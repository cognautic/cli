# Cognautic CLI Plugin Development Guide

Welcome to the Cognautic CLI Plugin Development Guide! This document will help you create powerful plugins to extend Cognautic's functionality.

## Table of Contents

1. [Introduction](#introduction)
2. [Plugin Structure](#plugin-structure)
3. [Creating Your First Plugin](#creating-your-first-plugin)
4. [Plugin API Reference](#plugin-api-reference)
5. [Registering Commands](#registering-commands)
6. [Registering Tools](#registering-tools)
7. [Hooks and Events](#hooks-and-events)
8. [Best Practices](#best-practices)
9. [Example Plugins](#example-plugins)

## Introduction

Cognautic CLI plugins allow you to:
- Add custom slash commands
- Register new tools for the AI to use
- Intercept and modify messages
- Access Cognautic's AI engine, config, and workspace
- Extend functionality without modifying core code

## Plugin Structure

Every plugin must follow this directory structure:

```
my-plugin/
├── plugin.json          # Plugin metadata (required)
└── my_plugin.py         # Plugin implementation (required)
```

### plugin.json

The `plugin.json` file contains metadata about your plugin:

```json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "description": "A sample plugin for Cognautic CLI",
  "author": "Your Name",
  "entry_point": "my_plugin.Plugin",
  "dependencies": []
}
```

**Fields:**
- `name`: Unique identifier for your plugin (lowercase, hyphens allowed)
- `version`: Semantic version (e.g., "1.0.0")
- `description`: Brief description of what your plugin does
- `author`: Your name or organization
- `entry_point`: Python module path to your plugin class (format: `module_name.ClassName`)
- `dependencies`: List of Python packages required (optional)

### Plugin Implementation

Your plugin must inherit from `BasePlugin` and implement the required methods:

```python
from cognautic.plugin_manager import BasePlugin, PluginAPI

class Plugin(BasePlugin):
    def __init__(self, api: PluginAPI):
        super().__init__(api)
        self.name = "my-plugin"
        self.version = "1.0.0"
        self.description = "A sample plugin"
    
    async def on_load(self):
        """Called when plugin is loaded"""
        # Register commands, tools, etc.
        pass
    
    async def on_unload(self):
        """Called when plugin is unloaded"""
        # Cleanup resources
        pass
    
    async def on_message(self, message: str, role: str):
        """Called for each message (optional)"""
        # Intercept/modify messages
        return None  # Return modified message or None
```

## Creating Your First Plugin

Let's create a simple "Hello World" plugin:

### Step 1: Create Plugin Directory

```bash
mkdir -p ~/.cognautic/plugins/hello-world
cd ~/.cognautic/plugins/hello-world
```

### Step 2: Create plugin.json

```json
{
  "name": "hello-world",
  "version": "1.0.0",
  "description": "A simple hello world plugin",
  "author": "Cognautic Team",
  "entry_point": "hello_world.Plugin"
}
```

### Step 3: Create hello_world.py

```python
from cognautic.plugin_manager import BasePlugin, PluginAPI

class Plugin(BasePlugin):
    def __init__(self, api: PluginAPI):
        super().__init__(api)
        self.name = "hello-world"
        self.version = "1.0.0"
        self.description = "A simple hello world plugin"
    
    async def on_load(self):
        """Register our custom command"""
        self.api.register_command(
            "hello",
            self.hello_command,
            "Say hello to the user"
        )
        self.api.print("✓ Hello World plugin loaded!", style="green")
    
    async def hello_command(self, args, context):
        """Handler for /hello command"""
        name = " ".join(args) if args else "World"
        self.api.print(f"Hello, {name}! 👋", style="bold cyan")
```

### Step 4: Install and Use

```bash
# In Cognautic CLI chat:
/plugin install ~/.cognautic/plugins/hello-world
/plugin load hello-world
/hello
/hello Cognautic
```

## Plugin API Reference

The `PluginAPI` class provides methods to interact with Cognautic:

### Command Registration

```python
api.register_command(command: str, handler: Callable, description: str = "")
```

Register a new slash command.

**Example:**
```python
async def my_handler(args, context):
    self.api.print(f"Args: {args}")

await self.api.register_command("mycommand", my_handler, "My custom command")
```

### Tool Registration

```python
api.register_tool(tool: BaseTool)
```

Register a new tool for the AI to use.

**Example:**
```python
from cognautic.tools.base import BaseTool, ToolResult, PermissionLevel

class MyTool(BaseTool):
    def __init__(self):
        super().__init__(
            name="my_tool",
            description="Does something useful",
            permission_level=PermissionLevel.SAFE_OPERATIONS
        )
    
    async def execute(self, **kwargs):
        # Tool implementation
        return ToolResult(success=True, data="Result")
    
    def get_capabilities(self):
        return ["capability1", "capability2"]

# In on_load:
self.api.register_tool(MyTool())
```

### Workspace and Context

```python
# Get current workspace path
workspace = api.get_workspace()

# Get current AI provider
provider = api.get_provider()

# Get current AI model
model = api.get_model()

# Get config manager
config = api.get_config_manager()

# Get AI engine
ai_engine = api.get_ai_engine()

# Get memory manager
memory = api.get_memory_manager()
```

### Printing to Console

```python
api.print(message: str, style: str = "")
```

Print messages with Rich formatting.

**Example:**
```python
self.api.print("Success!", style="green")
self.api.print("Warning!", style="yellow")
self.api.print("Error!", style="bold red")
```

### Executing Commands

```python
result = await api.execute_command(command: str)
```

Execute shell commands in the current workspace.

**Example:**
```python
result = await self.api.execute_command("ls -la")
if result['returncode'] == 0:
    self.api.print(result['stdout'])
```

### Asking the AI

```python
response = await api.ask_ai(prompt: str, **kwargs)
```

Send a prompt to the AI engine.

**Example:**
```python
response = await self.api.ask_ai(
    "Explain what this code does",
    provider="openai",
    model="gpt-4"
)
self.api.print(response)
```

## Registering Commands

Commands are registered in the `on_load` method:

```python
async def on_load(self):
    self.api.register_command(
        "mycommand",           # Command name (use without /)
        self.handle_command,   # Handler function
        "Command description"  # Help text
    )

async def handle_command(self, args, context):
    """
    Args:
        args: List of command arguments
        context: Dict with CLI context (workspace, provider, etc.)
    """
    self.api.print(f"Command called with args: {args}")
```

### Command Handler Context

The `context` dict contains:
- `current_workspace`: Current workspace path
- `provider`: Current AI provider
- `model`: Current AI model
- `config_manager`: Config manager instance
- `ai_engine`: AI engine instance
- `memory_manager`: Memory manager instance
- `confirmation_manager`: Confirmation manager instance

## Registering Tools

Tools extend the AI's capabilities:

```python
from cognautic.tools.base import BaseTool, ToolResult, PermissionLevel

class WeatherTool(BaseTool):
    def __init__(self):
        super().__init__(
            name="get_weather",
            description="Get weather for a location",
            permission_level=PermissionLevel.SAFE_OPERATIONS
        )
    
    async def execute(self, location: str = ""):
        """Execute the tool"""
        if not location:
            return ToolResult(
                success=False,
                error="Location is required"
            )
        
        # Fetch weather data (simplified)
        weather_data = f"Weather in {location}: Sunny, 72°F"
        
        return ToolResult(
            success=True,
            data=weather_data
        )
    
    def get_capabilities(self):
        return ["weather_lookup", "location_based_info"]

# Register in on_load:
async def on_load(self):
    self.api.register_tool(WeatherTool())
```

## Hooks and Events

### on_message Hook

Intercept and modify messages:

```python
async def on_message(self, message: str, role: str):
    """
    Args:
        message: The message content
        role: "user" or "assistant"
    
    Returns:
        Modified message or None to leave unchanged
    """
    # Example: Add timestamp to user messages
    if role == "user":
        from datetime import datetime
        timestamp = datetime.now().strftime("%H:%M:%S")
        return f"[{timestamp}] {message}"
    
    return None  # Don't modify assistant messages
```

## Best Practices

### 1. Error Handling

Always handle errors gracefully:

```python
async def my_command(self, args, context):
    try:
        # Your code here
        pass
    except Exception as e:
        self.api.print(f"Error: {e}", style="red")
```

### 2. Async/Await

All command handlers and hooks should be async:

```python
async def on_load(self):
    # Use await for async operations
    result = await self.api.execute_command("ls")
```

### 3. Resource Cleanup

Clean up resources in `on_unload`:

```python
async def on_unload(self):
    # Close connections, save state, etc.
    if hasattr(self, 'connection'):
        await self.connection.close()
```

### 4. User Feedback

Provide clear feedback to users:

```python
self.api.print("✓ Operation successful", style="green")
self.api.print("⚠ Warning: something happened", style="yellow")
self.api.print("✗ Error: operation failed", style="red")
```

### 5. Documentation

Document your commands:

```python
async def my_command(self, args, context):
    """
    My custom command
    
    Usage: /mycommand <arg1> <arg2>
    
    Examples:
        /mycommand hello world
        /mycommand --option value
    """
    if not args:
        self.api.print("Usage: /mycommand <arg1> <arg2>")
        return
```

## Example Plugins

### Example 1: Git Helper Plugin

```python
from cognautic.plugin_manager import BasePlugin, PluginAPI

class Plugin(BasePlugin):
    def __init__(self, api: PluginAPI):
        super().__init__(api)
        self.name = "git-helper"
        self.version = "1.0.0"
        self.description = "Git shortcuts and helpers"
    
    async def on_load(self):
        self.api.register_command("gstatus", self.git_status, "Show git status")
        self.api.register_command("gcommit", self.git_commit, "Quick commit")
    
    async def git_status(self, args, context):
        """Show git status"""
        result = await self.api.execute_command("git status --short")
        if result['returncode'] == 0:
            self.api.print(result['stdout'])
        else:
            self.api.print(f"Error: {result['stderr']}", style="red")
    
    async def git_commit(self, args, context):
        """Quick commit with message"""
        if not args:
            self.api.print("Usage: /gcommit <message>", style="yellow")
            return
        
        message = " ".join(args)
        
        # Stage all changes
        await self.api.execute_command("git add .")
        
        # Commit
        result = await self.api.execute_command(f'git commit -m "{message}"')
        
        if result['returncode'] == 0:
            self.api.print("✓ Committed successfully!", style="green")
        else:
            self.api.print(f"Error: {result['stderr']}", style="red")
```

### Example 2: Code Snippet Plugin

```python
from cognautic.plugin_manager import BasePlugin, PluginAPI
import json
from pathlib import Path

class Plugin(BasePlugin):
    def __init__(self, api: PluginAPI):
        super().__init__(api)
        self.name = "snippets"
        self.version = "1.0.0"
        self.description = "Save and use code snippets"
        self.snippets_file = Path.home() / ".cognautic" / "snippets.json"
        self.snippets = {}
    
    async def on_load(self):
        # Load snippets
        if self.snippets_file.exists():
            with open(self.snippets_file, 'r') as f:
                self.snippets = json.load(f)
        
        self.api.register_command("snippet", self.snippet_command, "Manage code snippets")
    
    async def snippet_command(self, args, context):
        """Manage snippets: /snippet [save|list|get|delete] <name> [code]"""
        if not args:
            self.api.print("Usage: /snippet [save|list|get|delete] <name> [code]")
            return
        
        action = args[0]
        
        if action == "list":
            if not self.snippets:
                self.api.print("No snippets saved", style="dim")
            else:
                self.api.print("Saved snippets:", style="bold")
                for name in self.snippets:
                    self.api.print(f"  • {name}")
        
        elif action == "save" and len(args) >= 3:
            name = args[1]
            code = " ".join(args[2:])
            self.snippets[name] = code
            self._save_snippets()
            self.api.print(f"✓ Saved snippet: {name}", style="green")
        
        elif action == "get" and len(args) >= 2:
            name = args[1]
            if name in self.snippets:
                self.api.print(f"Snippet '{name}':", style="bold")
                self.api.print(self.snippets[name])
            else:
                self.api.print(f"Snippet '{name}' not found", style="red")
        
        elif action == "delete" and len(args) >= 2:
            name = args[1]
            if name in self.snippets:
                del self.snippets[name]
                self._save_snippets()
                self.api.print(f"✓ Deleted snippet: {name}", style="green")
            else:
                self.api.print(f"Snippet '{name}' not found", style="red")
    
    def _save_snippets(self):
        self.snippets_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.snippets_file, 'w') as f:
            json.dump(self.snippets, f, indent=2)
```

## Installing Plugins

### From Local Directory

```bash
/plugin install /path/to/plugin-directory
```

### From Current Directory

```bash
/plugin install ./my-plugin
```

### From Home Directory

```bash
/plugin install ~/my-plugins/awesome-plugin
```

## Managing Plugins

### List Installed Plugins

```bash
/plugin list
```

### Load a Plugin

```bash
/plugin load plugin-name
```

### Unload a Plugin

```bash
/plugin unload plugin-name
```

### Get Plugin Info

```bash
/plugin info plugin-name
```

### Uninstall a Plugin

```bash
/plugin uninstall plugin-name
```

## Troubleshooting

### Plugin Not Loading

1. Check `plugin.json` is valid JSON
2. Verify `entry_point` matches your class name
3. Check for syntax errors in your Python file
4. Look for error messages in the console

### Command Not Working

1. Ensure command is registered in `on_load`
2. Check command handler is async
3. Verify command name doesn't conflict with existing commands

### Import Errors

1. Check all required packages are installed
2. Verify import paths are correct
3. Ensure plugin directory is in Python path

## Support

For more help:
- GitHub Issues: https://github.com/cognautic/cli/issues
- Documentation: https://cognautic.vercel.app
- Examples: Check the `examples/plugins` directory

Happy plugin development! 🚀
