"""
Confirmation handler for AI operations
"""

from rich.console import Console
from prompt_toolkit import PromptSession
from prompt_toolkit.key_binding import KeyBindings
import asyncio
from typing import Callable, Optional

console = Console()


class ConfirmationManager:
    """Manages confirmation prompts for AI operations"""
    
    def __init__(self):
        self.yolo_mode = False  # Default: require confirmation
        bindings = KeyBindings()

        @bindings.add("c-y")
        def _toggle_yolo(event):
            self.toggle_yolo_mode()
            event.app.exit(result="__TOGGLE_YOLO__")

        self.session = PromptSession(key_bindings=bindings)
        self._on_prompt_start: Optional[Callable[[], None]] = None
        self._on_prompt_end: Optional[Callable[[], None]] = None
    
    def toggle_yolo_mode(self):
        """Toggle YOLO mode on/off"""
        self.yolo_mode = not self.yolo_mode
        return self.yolo_mode
    
    def set_yolo_mode(self, enabled: bool):
        """Set YOLO mode state"""
        self.yolo_mode = enabled
    
    def is_yolo_mode(self) -> bool:
        """Check if YOLO mode is enabled"""
        return self.yolo_mode

    def set_prompt_hooks(
        self,
        on_prompt_start: Optional[Callable[[], None]] = None,
        on_prompt_end: Optional[Callable[[], None]] = None,
    ):
        """Set callbacks to run around interactive confirmation prompts."""
        self._on_prompt_start = on_prompt_start
        self._on_prompt_end = on_prompt_end
    
    async def confirm_operation(self, operation_type: str, details: dict) -> bool:
        """
        Ask user to confirm an operation
        
        Args:
            operation_type: Type of operation (file_operation, command_runner, etc.)
            details: Dictionary with operation details
        
        Returns:
            True if confirmed, False if cancelled
        """
        # If YOLO mode is enabled, auto-confirm everything
        if self.yolo_mode:
            return True
        
        # Format the confirmation prompt based on operation type
        if operation_type == "file_operations":
            operation = details.get("operation", "unknown")
            file_path = details.get("file_path", "unknown")
            
            # Different colors for different operations
            if operation in ["write_file", "write_file_lines", "create_file"]:
                color = "yellow"
                icon = "INFO:"
            elif operation == "delete_file":
                color = "red"
                icon = "WARNING:"
            elif operation in ["read_file", "read_file_lines", "list_directory"]:
                # Auto-confirm read operations
                return True
            else:
                color = "cyan"
                icon = "INFO:"
            
            console.print(f"\n[{color}]{icon} AI wants to perform file operation:[/{color}]")
            console.print(f"  Operation: [bold]{operation}[/bold]")
            console.print(f"  File: [bold]{file_path}[/bold]")
            
            # Show content preview for write operations
            if operation in ["write_file", "write_file_lines"] and "content" in details:
                content = details["content"]
                preview = content[:200] + "..." if len(content) > 200 else content
                console.print(f"  Content preview:\n[dim]{preview}[/dim]")
        
        elif operation_type == "command_runner":
            command = details.get("command", "unknown")
            cwd = details.get("cwd", ".")
            operation = details.get("operation", "run_command")
            
            icon = "INFO:" if operation == "run_async_command" else "INFO:"
            console.print(f"\n[yellow]{icon} AI wants to run command:[/yellow]")
            console.print(f"  Command: [bold]{command}[/bold]")
            console.print(f"  Directory: [dim]{cwd}[/dim]")
            if operation == "run_async_command":
                console.print(f"  Mode: [bold]Background[/bold]")
        
        else:
            # Generic confirmation for other operations
            console.print(f"\n[cyan]INFO: AI wants to perform operation:[/cyan]")
            console.print(f"  Type: [bold]{operation_type}[/bold]")
            for key, value in details.items():
                if key != "content":  # Don't show full content
                    console.print(f"  {key}: {value}")
        
        # Strict y/n confirmation loop: block tool execution until explicit decision.
        console.print("\n[bold green]Accept?[/bold green] Type [bold]y[/bold] to confirm or [bold]n[/bold] to reject.")

        if self._on_prompt_start:
            self._on_prompt_start()
        try:
            while True:
                try:
                    user_input = await self.session.prompt_async("Confirm [y/n]: ")
                except (KeyboardInterrupt, EOFError):
                    console.print("[red]CANCELLED: Operation cancelled[/red]")
                    return False

                answer = (user_input or "").strip().lower()
                if user_input == "__TOGGLE_YOLO__":
                    self.display_mode_status()
                    if self.yolo_mode:
                        console.print("[green]SUCCESS: Confirmed (YOLO mode enabled)[/green]")
                        return True
                    continue
                if answer in {"y", "yes"}:
                    console.print("[green]SUCCESS: Confirmed[/green]")
                    return True
                if answer in {"n", "no"}:
                    console.print("[red]CANCELLED: Operation cancelled[/red]")
                    return False

                console.print("[yellow]Please type 'y' or 'n'.[/yellow]")
        finally:
            if self._on_prompt_end:
                self._on_prompt_end()
    
    def display_mode_status(self):
        """Display current confirmation mode status"""
        if self.yolo_mode:
            console.print("[bold yellow]INFO: YOLO MODE: ON[/bold yellow] - AI operations will execute without confirmation")
        else:
            console.print("[bold green]INFO: SAFE MODE: ON[/bold green] - AI operations require confirmation")
