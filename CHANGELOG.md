# Changelog

All notable changes to Cognautic CLI will be documented in this file.

## [1.1.6] - 2025-11-12

### Added
- **Command Auto-Completion**
  - Implemented slash command auto-completion using Tab key
  - Shows available commands with descriptions as you type
  - Automatically filters commands based on what you've typed
  - Works with all slash commands (e.g., /help, /workspace, /model, etc.)
  - Displays command descriptions in the completion menu
  
- **Confirmation Feature for AI Operations**
  - Implemented Safe Mode (default) that prompts user for confirmation before AI executes destructive operations
  - Added YOLO Mode for experienced users who want AI to execute operations without confirmation
  - `/yolo` command to toggle between Safe and YOLO modes
  - `Ctrl+Y` keybinding for quick mode switching during chat
  - Visual status indicators showing current confirmation mode
  - Smart confirmation logic:
    - File operations: Confirms write, create, delete, move, copy operations
    - File operations: Auto-approves read-only operations (read_file, list_directory)
    - Command execution: Confirms all command runs (both foreground and background)
  - Rich confirmation prompts with:
    - Color-coded operation types
    - Preview of file content for write operations
    - Command details and working directory
    - Clear instructions (ENTER to confirm, ESC to cancel)
  - Updated help documentation with confirmation mode information

### Changed
- AI engine now accepts `confirmation_manager` parameter throughout the tool execution pipeline
- Tool execution methods updated to check confirmation mode before executing operations
- Help text updated to include new `/yolo` command and `Ctrl+Y` keybinding

### Technical Details
- New class: `SlashCommandCompleter` in `cognautic/cli.py` - Implements prompt_toolkit Completer interface
- New module: `cognautic/confirmation.py` - Manages confirmation state and user prompts
- Modified: `cognautic/cli.py` - Integrated confirmation manager and command completer into chat session
- Modified: `cognautic/ai_engine.py` - Added confirmation checks in:
  - `_execute_single_tool_live()` method
  - `_process_response_with_tools()` method
  - `_stream_with_live_tools()` method
  - `process_message_stream()` method
