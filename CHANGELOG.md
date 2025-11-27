# Changelog

All notable changes to Cognautic CLI will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2025-11-27

### Added - Plugin System 🔌

**Comprehensive Plugin Architecture for Extending Cognautic CLI**

This major update introduces a complete plugin system that allows users to extend Cognautic CLI with custom commands, tools, and functionality without modifying the core codebase.

#### Key Features

- **Plugin Manager** - Complete lifecycle management for plugins (install, load, unload, uninstall)
- **Plugin API** - Rich API providing plugins access to:
  - Command registration (custom slash commands)
  - Tool registration (extend AI capabilities)
  - AI engine (ask AI questions, process prompts)
  - Workspace and configuration access
  - Console output with Rich formatting
- **Auto-Loading** - Plugins are automatically loaded at startup and when installed
- **Natural Language Integration** - Plugins can use AI naturally without forcing JSON responses

#### Plugin System Components

**Core Files:**
- `cognautic/plugin_manager.py` - Plugin manager, API, and base plugin class
- Plugin commands integrated into `cognautic/cli.py`

**Documentation:**
- `PLUGIN_DEVELOPMENT.md` - Comprehensive plugin development guide
- `examples/plugins/README.md` - Plugin examples and quick start
- `PLUGIN_SYSTEM_SUMMARY.md` - Implementation overview

#### Example Plugins Included

**1. Hello World Plugin** (`examples/plugins/hello-world/`)
- Demonstrates basic plugin structure
- Shows command registration and context access
- Includes message interception hooks
- Commands: `/hello`, `/greet`, `/stats`

**2. Debug Assistant Plugin** (`examples/plugins/debug-assistant/`)
- AI-powered code analysis and bug detection
- Multi-language support (Python, JavaScript, TypeScript, Java, C/C++, Go, Rust, Ruby, PHP, Swift, Kotlin, C#, Scala)
- Natural language bug reports with severity levels
- Auto-fix capability using AI
- Commands: `/debug`, `/debugfile`

#### Plugin Commands

```bash
/plugin install <path>    # Install and auto-load a plugin
/plugin list              # List all installed plugins
/plugin load <name>       # Load a plugin
/plugin unload <name>     # Unload a plugin
/plugin uninstall <name>  # Uninstall a plugin
/plugin info <name>       # Show plugin information
```

#### Usage Example

```bash
# Install the debug assistant plugin
/plugin install examples/plugins/debug-assistant

# Plugin is automatically loaded and ready to use
/debug                    # Analyze workspace for bugs
/debugfile test.js --fix  # Analyze and fix specific file
```

#### Technical Implementation

**Plugin Structure:**
```
my-plugin/
├── plugin.json          # Metadata (name, version, description, entry point)
└── my_plugin.py         # Implementation (inherits from BasePlugin)
```

**Plugin Lifecycle Hooks:**
- `on_load()` - Called when plugin is loaded
- `on_unload()` - Called when plugin is unloaded
- `on_message(message, role)` - Intercept and modify messages

**Plugin API Methods:**
- `register_command(command, handler, description)` - Add custom commands
- `register_tool(tool)` - Add tools for AI
- `get_workspace()`, `get_provider()`, `get_model()` - Access context
- `print(message, style)` - Console output
- `execute_command(cmd)` - Run shell commands
- `ask_ai(prompt)` - Interact with AI

#### Bug Fixes

- Fixed plugin API initialization timing
- Fixed TypeError in print() calls
- Improved AI response parsing for natural language
- Fixed plugin output covering prompt (async lifecycle)
- Auto-load plugins at startup and on install

#### Benefits

- **Extensibility** - Add features without modifying core code
- **Modularity** - Self-contained, independent plugins
- **Community** - Share and distribute plugins easily
- **AI Integration** - Full access to Cognautic's AI capabilities
- **Simple Workflow** - Install once, use immediately

---