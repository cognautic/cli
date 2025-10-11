# Cognautic CLI

**A Python-based CLI AI coding agent that provides agentic development capabilities with multi-provider AI support and real-time interaction.**

⚠️ **Under Development** - Some features may be unavailable

---

## Overview

Cognautic CLI is a Python-based command-line interface that brings AI-powered development capabilities directly to your terminal. It provides agentic tools for file operations, command execution, web search, and code analysis with support for multiple AI providers. The tool is accessed through a single `cognautic` command with various subcommands.

## ⚠️ Coming Soon - Not Yet Released

> **IMPORTANT:** Cognautic CLI is currently in active development and **has not been released yet**. This documentation is a preview of upcoming features. The tool will be available for download soon. Follow this repository for updates on the release.

> **⚠️ Development Notice:** Cognautic CLI is currently under development. Some features may be unavailable or subject to change.

### Project Information

| Property | Value |
|----------|-------|
| **Developer** | Cognautic Team |
| **Written in** | Python |
| **Operating system** | Cross-platform |
| **Type** | AI Development Tool |
| **Status** | Under Development |
| **Repository** | [github.com/cognautic/cli](https://github.com/cognautic/cli) |

---

## Features

- **Multi-Provider AI Support**: Integrate with OpenAI, Anthropic, Google, Together AI, OpenRouter, and 15+ other AI providers
- **Agentic Tools**: File operations, command execution, web search, and code analysis
- **Real-time Communication**: WebSocket server for live AI responses and tool execution
- **Secure Configuration**: Encrypted API key storage and permission management
- **Interactive CLI**: Rich terminal interface with progress indicators, colored output, and command history

---

## Installation

### Prerequisites

Ensure you have Python 3.8 or higher installed:

```bash
python --version
```

### Download the Wheel File

Download the latest `.whl` file from the official repository:

```bash
# Visit https://github.com/cognautic/cli/releases
# Download the latest cognautic_cli-z.z.z-py3-none-any.whl file
```

### Installation with pip

Install the downloaded wheel file using pip:

```bash
# Navigate to your downloads folder
cd ~/Downloads

# Install the wheel file
pip install cognautic_cli-z.z.z-py3-none-any.whl
```

### Installation with pipx (Recommended)

For isolated installation, use pipx:

```bash
# Install pipx if you don't have it
pip install pipx
pipx ensurepath

# Install Cognautic CLI with pipx
pipx install cognautic_cli-z.z.z-py3-none-any.whl
```

### Verify Installation

Check that Cognautic CLI is installed correctly:

```bash
cognautic --version
```

### Updating Cognautic CLI

To update to a newer version, download the new wheel file and:

```bash
# With pip (force reinstall)
pip install cognautic_cli-y.y.y-py3-none-any.whl --force-reinstall

# With pipx
pipx upgrade cognautic-cli
# Or force reinstall with pipx
pipx install cognautic_cli-y.y.y-py3-none-any.whl --force
```

_**Note:** Replace `y.y.y` and `z.z.z` with actual version numbers (e.g., 1.2.0, 2.1.5)._

### Uninstallation

To remove Cognautic CLI:

```bash
# With pip
pip uninstall cognautic-cli

# With pipx
pipx uninstall cognautic-cli
```

---

## Quick Start - The Easy Way

The simplest way to use Cognautic CLI is to just run the main command and do everything interactively:

### Step 1: Run Cognautic

```bash
cognautic
```

This single command launches the interactive Cognautic CLI interface where you can:

- Set up your API keys on first run
- Choose your preferred AI provider
- Start chatting with AI agents
- Build projects from natural language descriptions
- Analyze existing code
- Configure all settings

### Step 2: Follow the Interactive Setup

On first run, Cognautic will guide you through:

1. Welcome screen and version check
2. API key configuration for your preferred providers
3. Basic preferences setup
4. Quick tutorial of available commands

### Step 3: Start Using AI

Once inside the CLI, you can use simple commands like:

```bash
# Chat with AI
/chat

# Build a new project
/build "Create a web scraper"

# Analyze current directory
/analyze

# Get help
/help
```

**That's it!** No complex command-line arguments needed. Everything happens interactively within the Cognautic interface.

---

## Interactive Commands

Once you run `cognautic`, you'll be in the interactive CLI where you can use these simple commands:

### Chat Commands

```bash
/chat                # Start chatting with AI
/chat anthropic      # Chat with specific provider
/switch openai       # Switch AI provider
/model gpt-4         # Change model
```

### Project Building

```bash
/build "description" # Build project from description
/build               # Interactive project builder
/template web        # Use project template
```

### Code Analysis

```bash
/analyze             # Analyze current directory
/analyze ./path      # Analyze specific path
/suggestions         # Get improvement suggestions
/security            # Security analysis
```

### Configuration

```bash
/setup               # Run setup wizard
/providers           # List available providers
/keys                # Manage API keys
/settings            # View/change settings
/help                # Show all commands
/exit                # Exit Cognautic
```

---

## Advanced Command-Line Usage

For automation and scripting, you can also use Cognautic with direct command-line arguments:

### Setup

```bash
cognautic setup --interactive           # Interactive setup
cognautic setup --provider openai       # Quick provider setup
```

### Direct Chat

```bash
cognautic chat --provider anthropic --model claude-3-sonnet
cognautic chat --project-path ./my_project
```

### Direct Build

```bash
cognautic build "Create a FastAPI web app" --language python
cognautic build "React dashboard" --framework react --output-dir ./dashboard
```

### Direct Analysis

```bash
cognautic analyze ./my_project --suggestions
cognautic analyze . --focus security --output-format json
```

### Provider Management

```bash
cognautic providers                              # List all providers
cognautic config set default_provider anthropic
```

---

## Supported AI Providers

| Provider | Models | API Key Required |
|----------|--------|------------------|
| **OpenAI** | GPT models (GPT-4, GPT-3.5) | `OPENAI_API_KEY` |
| **Anthropic** | Claude models (Claude-3 Sonnet, Haiku) | `ANTHROPIC_API_KEY` |
| **Google** | Gemini models | `GOOGLE_API_KEY` |
| **Together AI** | Various open-source models | `TOGETHER_API_KEY` |
| **OpenRouter** | Access to multiple providers | `OPENROUTER_API_KEY` |

---

## Configuration

Configuration files are stored in `~/.cognautic/`:

- `config.json`: General settings and preferences
- `api_keys.json`: Encrypted API keys for AI providers
- `sessions/`: Chat session history and context
- `cache/`: Temporary files and model cache

---

## Command Usage

All Cognautic CLI functionality is accessed through the single `cognautic` command. The general syntax is:

```bash
cognautic <subcommand> [options] [arguments]
```

### Getting Help

```bash
# Show general help
cognautic --help

# Show help for specific command
cognautic chat --help
cognautic build --help
```

### Version Information

```bash
cognautic --version
```

---

## Examples

### Simple Interactive Session

The easiest way to get started:

```bash
$ cognautic
🚀 Welcome to Cognautic CLI
📁 Current directory: /home/user/projects
💡 Type '/help' for commands, '/exit' to quit

cognautic> /build "Create a simple todo app in Python"
🤖 Building your project...
✅ Created todo_app/ with 5 files

cognautic> /analyze todo_app
🔍 Analyzing code structure...
✅ Analysis complete. Found 3 suggestions.

cognautic> /chat
💬 Starting chat session...
You: How can I add a database to this todo app?
AI: I can help you integrate SQLite...
```

### First-Time Setup

```bash
$ cognautic
🎉 Welcome to Cognautic! Let's get you set up.
🔑 No API keys found. Let's configure them.

Which AI provider would you like to use?
1. OpenAI (GPT-4, GPT-3.5)
2. Anthropic (Claude)
3. Google (Gemini)
4. Other providers...

Choice [1-4]: 2
🔐 Please enter your Anthropic API key: sk-ant-...
✅ API key saved securely!

🚀 Setup complete! You're ready to go.
```

### Building Different Project Types

```bash
cognautic> /build "React dashboard with charts"
cognautic> /build "Python API with FastAPI"
cognautic> /build "Node.js Discord bot"
cognautic> /template # Browse templates
cognautic> /build     # Interactive builder
```

### Advanced Command-Line Usage

For scripting and automation:

```bash
# Direct project creation
cognautic build "FastAPI web app" --language python --output-dir ./api

# Batch analysis
cognautic analyze ./projects --output-format json > analysis.json

# Automated chat session
echo "Explain this code" | cognautic chat --project-path ./my_app
```

---

## License

Proprietary - All Rights Reserved

© 2025 Cognautic Team

For licensing inquiries, contact: cognautic@gmail.com
