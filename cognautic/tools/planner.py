"""
Planner tools for exposing task steps and progress updates to the user.
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict, List
from uuid import uuid4

from .base import BaseTool, PermissionLevel, ToolResult


def _validate_steps(raw_steps: Any) -> List[Dict[str, Any]]:
    if not isinstance(raw_steps, list) or not raw_steps:
        raise ValueError("steps must be a non-empty list")

    normalized_steps: List[Dict[str, Any]] = []
    for index, step in enumerate(raw_steps, start=1):
        if not isinstance(step, dict):
            raise ValueError("each step must be an object")

        title = str(step.get("step", "")).strip()
        if not title:
            raise ValueError(f"step {index} is missing a non-empty 'step' value")

        status = str(step.get("status", "pending")).strip().lower()
        if status not in {"pending", "in_progress", "completed"}:
            raise ValueError(
                f"step {index} has invalid status '{status}'; use pending, in_progress, or completed"
            )

        normalized_steps.append(
            {
                "id": step.get("id") or f"step_{index}",
                "step": title,
                "status": status,
            }
        )

    in_progress_count = sum(1 for step in normalized_steps if step["status"] == "in_progress")
    if in_progress_count > 1:
        raise ValueError("at most one step can be in_progress")

    return normalized_steps


class PlannerTool(BaseTool):
    """Create a visible task plan for the current request."""

    def __init__(self):
        super().__init__(
            name="planner",
            description="Create a visible step-by-step plan for the current task before substantial work begins",
            permission_level=PermissionLevel.READ_ONLY,
        )
        self.plans: Dict[str, Dict[str, Any]] = {}

    def get_capabilities(self) -> List[str]:
        return ["create_plan", "get_plan"]

    def get_schema(self) -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "planner",
                "description": "Create a short execution plan for the task so the user can see the intended steps.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "objective": {
                            "type": "string",
                            "description": "Short summary of the user task being executed",
                        },
                        "steps": {
                            "type": "array",
                            "description": "Ordered plan steps. Keep them concrete and short.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "id": {
                                        "type": "string",
                                        "description": "Optional stable step identifier",
                                    },
                                    "step": {
                                        "type": "string",
                                        "description": "Human-readable step description",
                                    },
                                    "status": {
                                        "type": "string",
                                        "enum": ["pending", "in_progress", "completed"],
                                        "description": "Initial status for the step",
                                    },
                                },
                                "required": ["step"],
                            },
                        },
                    },
                    "required": ["objective", "steps"],
                },
            },
        }

    async def execute(self, objective: str, steps: List[Dict[str, Any]], **kwargs) -> ToolResult:
        normalized_steps = _validate_steps(steps)
        plan_id = f"plan_{uuid4().hex[:8]}"
        plan = {
            "plan_id": plan_id,
            "objective": objective.strip(),
            "steps": normalized_steps,
        }
        self.plans[plan_id] = deepcopy(plan)
        return ToolResult(success=True, data=plan)


class UpdatePlanTool(BaseTool):
    """Update plan status so the user can track progress."""

    def __init__(self, planner_tool: PlannerTool):
        super().__init__(
            name="update_plan",
            description="Update the visible progress of a previously created plan",
            permission_level=PermissionLevel.READ_ONLY,
        )
        self.planner_tool = planner_tool

    def get_capabilities(self) -> List[str]:
        return ["update_plan"]

    def get_schema(self) -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_plan",
                "description": "Update plan step statuses as work progresses. Use the existing plan_id returned by planner.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {
                            "type": "string",
                            "description": "The plan identifier returned by planner",
                        },
                        "explanation": {
                            "type": "string",
                            "description": "Optional brief explanation of the progress update",
                        },
                        "steps": {
                            "type": "array",
                            "description": "Full updated step list with current statuses.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "id": {
                                        "type": "string",
                                        "description": "Stable step identifier from the original plan",
                                    },
                                    "step": {
                                        "type": "string",
                                        "description": "Human-readable step description",
                                    },
                                    "status": {
                                        "type": "string",
                                        "enum": ["pending", "in_progress", "completed"],
                                        "description": "Current status for the step",
                                    },
                                },
                                "required": ["step", "status"],
                            },
                        },
                    },
                    "required": ["plan_id", "steps"],
                },
            },
        }

    async def execute(
        self, plan_id: str, steps: List[Dict[str, Any]], explanation: str = "", **kwargs
    ) -> ToolResult:
        if plan_id not in self.planner_tool.plans:
            return ToolResult(success=False, error=f"Unknown plan_id: {plan_id}")

        normalized_steps = _validate_steps(steps)
        stored_plan = self.planner_tool.plans[plan_id]
        stored_plan["steps"] = normalized_steps
        if explanation.strip():
            stored_plan["last_update"] = explanation.strip()

        return ToolResult(
            success=True,
            data={
                "plan_id": plan_id,
                "objective": stored_plan["objective"],
                "explanation": explanation.strip(),
                "steps": deepcopy(normalized_steps),
            },
        )
