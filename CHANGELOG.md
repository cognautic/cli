# Changelog

All notable changes to Cognautic CLI will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.4] - 2025-11-10

### Added

#### Smart Auto-Continuation System
- **Intelligent Auto-Continuation**: AI now automatically continues responses until task completion without manual intervention
- **Promise Detection**: System detects when AI says it will use a tool but doesn't execute it, automatically prompting for actual execution
- **Smart Prompting**: When AI forgets to execute tools, system provides helpful reminders with example JSON format
- **Simplified Logic**: Reduced from 10+ complex continuation rules to 5 simple rules for better reliability

#### Multi-Line Input Support
- **Alt+Enter for New Lines**: Press Alt+Enter to add new lines without sending the message
- **Enter to Send**: Press Enter to submit the complete message to AI
- **Paste Support**: Multi-line code blocks and text can now be pasted correctly without each line being sent separately
- **Visual Feedback**: Clear instructions shown on startup and in help menu

#### Double Ctrl+C Exit
- **Safe Exit**: Press Ctrl+C twice within 2 seconds to exit CLI
- **Accidental Press Protection**: Single Ctrl+C shows a hint message instead of exiting
- **Clear Feedback**: User receives clear instructions after first Ctrl+C press
- **Timer Reset**: 2-second window resets if not pressed again in time

#### New Code Navigation Tools
- **Smart Code Navigation Tool**: Jump to definitions, find references, and search symbols across codebase
  - `jump_to_definition`: Find where symbols are defined
  - `find_references`: Find all usages of a symbol
  - `search_symbols`: Search for symbols by name/pattern with type filtering
  - `list_symbols`: List all symbols in a file
  - `find_implementations`: Find class implementations and subclasses
  - `get_symbol_info`: Get detailed information about symbols
- **Language Support**: Full AST parsing for Python, regex patterns for JavaScript/TypeScript, basic support for Java, C/C++, Go, Rust, Ruby, PHP
- **Context Extraction**: Provides surrounding code context and symbol signatures

#### Automatic Directory Context
- **Auto-Loaded Context**: AI automatically receives current directory contents when starting a chat session
- **Real-Time Awareness**: AI knows about all files and folders without needing to run `ls` or `dir`
- **Smart Display**: Shows file sizes, directory item counts, and organized structure
- **Performance**: Lightweight scanning that doesn't impact startup time

#### Directory Context Tool
- **Comprehensive Directory Operations**:
  - `get_current_directory`: List immediate directory contents with metadata
  - `list_directory_tree`: Recursive tree view with configurable depth
  - `get_directory_summary`: Statistics including file counts, sizes, types, largest/recent files
  - `get_file_types`: Breakdown of file types with counts and sizes
  - `get_project_structure`: Intelligent project type detection (Python, Node.js, Rust, Go, Java, Ruby, PHP, C/C++, Web)
- **Smart Filtering**: Automatic exclusion of build/cache directories (`__pycache__`, `node_modules`, `.git`, etc.)
- **Permission Handling**: Graceful handling of permission errors

### Changed

#### Auto-Continuation Behavior
- **Always Continue**: System now continues after EVERY AI response unless `end_response` tool is called
- **No Manual "Continue"**: Eliminated need for users to type "continue" manually
- **Enhanced System Prompt**: Updated AI instructions to clearly explain auto-continuation behavior and importance of `end_response` tool
- **Better Loop Detection**: Improved detection of when AI is stuck in repetitive patterns

#### Input Handling
- **Simplified Key Bindings**: Removed complex signal handling in favor of straightforward prompt_toolkit bindings
- **Natural Behavior**: Ctrl+C now behaves like standard CLI tools (double-tap to exit)
- **Better UX**: Clear visual feedback for all key combinations

#### System Prompt
- **Directory Context Integration**: System prompt now includes automatic directory listing for better AI context
- **Tool Documentation**: Added comprehensive examples for new `directory_context` and `code_navigation` tools
- **Workflow Examples**: Enhanced examples showing how to use new tools effectively
- **Continuation Instructions**: Clear explanation that AI will keep being called until `end_response` is used

### Fixed

- **Multi-Line Paste Issue**: Fixed bug where pasting multi-line content would send each line as a separate message
- **Enter Key Behavior**: Fixed Enter key creating new lines instead of sending messages when multi-line mode was enabled
- **Ctrl+C Exit**: Fixed Ctrl+C not properly exiting CLI when idle
- **AI Promise Detection**: Fixed issue where AI would say "I will use X tool" but never actually execute it
- **Auto-Continuation Logic**: Simplified and fixed overly complex continuation rules that sometimes prevented task completion

### Removed

- **AI Stop Functionality**: Removed unreliable Ctrl+X/Alt+C stop AI response feature
- **Complex Signal Handlers**: Removed complicated SIGINT/SIGQUIT handling that caused conflicts
- **Redundant Continuation Rules**: Removed 10+ complex rules in favor of 5 simple, reliable rules

### Technical Details

#### Files Modified
- `cognautic/auto_continuation.py`: Completely rewrote continuation logic
- `cognautic/ai_engine.py`: Added directory context injection and tool documentation
- `cognautic/cli.py`: Implemented multi-line input and double Ctrl+C exit
- `cognautic/tools/__init__.py`: Added new tool imports
- `cognautic/tools/registry.py`: Registered new tools

#### Files Created
- `cognautic/tools/directory_context.py`: New directory context tool (367 lines)
- `cognautic/tools/code_navigation.py`: New code navigation tool (726 lines)
- `docs/NEW_FEATURES.md`: Comprehensive documentation for new features

#### Key Bindings
- **Enter**: Send message (submit input)
- **Alt+Enter**: New line (multi-line input)
- **Ctrl+C** (twice): Exit CLI (within 2 seconds)
- **Shift+Tab**: Toggle Chat/Terminal mode

### Performance
- **Faster Responses**: Auto-continuation eliminates wait time for manual "continue" commands
- **Better Context**: Directory context reduces unnecessary tool calls for file exploration
- **Efficient Scanning**: Directory scanning is depth-limited and uses lazy evaluation

### Documentation
- Added `NEW_FEATURES.md` with detailed feature documentation
- Added `MULTI_LINE_INPUT_FIX.md` explaining input handling
- Added `AUTO_CONTINUATION_UPDATE.md` documenting continuation system
- Added `DOUBLE_CTRL_C_EXIT.md` explaining exit behavior
- Updated help command with new key bindings

---

## [1.1.3] - Previous Release

(Previous changelog entries would go here)
