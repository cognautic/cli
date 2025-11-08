# Changelog

All notable changes to Cognautic CLI will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.2] - 2025-11-08

### Added - Major Features

#### 🎯 Terminal Mode with Mode Switching
- **Interactive Terminal Mode**: Press `Shift+Tab` to toggle between Chat mode (💬) and Terminal mode (🖥️)
- **Seamless Mode Switching**: Switch modes instantly without restarting the session
- **Mode Indicators**: Clear visual indicators showing current mode in the prompt
- **Immediate Prompt Display**: Prompt appears instantly after mode switch
- **Documentation**: Complete guide in `TERMINAL_MODE.md`

#### 🔄 Live Response Streaming with Real-Time Tool Execution
- **True Streaming**: AI response streams character-by-character as it's generated
- **Immediate Tool Execution**: Tools execute as soon as they're detected in the stream
- **Live Tool Results**: See command outputs and file operations in real-time
- **Real-Time Error Handling**: Errors appear immediately during streaming
- **Smart Tool Detection**: Detects JSON tool blocks while streaming and executes instantly
- **Fallback Support**: Gracefully falls back to non-streaming for providers that don't support it
- **Documentation**: Complete guide in `LIVE_RESPONSE.md`

#### 🧠 Smart Auto-Continuation System
- **Intelligent Continuation Logic**: Only continues when it makes logical sense
- **Exploratory Command Detection**: Recognizes exploration commands (ls, pwd, dir, etc.) and continues to do actual work
- **Context-Aware Decisions**: 
  - Continues after file creation to run necessary commands (npm install, pip install)
  - Continues after exploratory commands to complete the actual task
  - Continues when errors occur to let AI handle them
  - Stops when background processes are running
  - Stops when task is complete
- **AI Control**: Respects `end_response` tool calls to prevent unnecessary continuation
- **Safety Limits**: Maximum recursion depth (10) and iteration count (50) to prevent infinite loops
- **Early Iteration Support**: Continues for first 3 iterations to ensure task completion
- **Documentation**: Complete guide in `SMART_AUTO_CONTINUATION.md`

#### 🔧 Background Command Execution
- **Async Command Support**: Run long-running commands in the background
- **Process Management**: Track and manage background processes
- **Process IDs**: Each background process gets a unique ID and PID
- **Process Listing**: Use `/ps` to list all running background processes
- **Process Termination**: Use `/ct <process_id>` to terminate specific processes
- **Status Tracking**: Monitor process status (running, completed, failed)
- **Output Capture**: Capture stdout and stderr from background processes

#### 📁 File Reader & Grep Tools
- **File Reading**: Read entire files or specific line ranges
- **Grep Search**: Search for patterns in files with regex support
- **Line Range Reading**: Read specific sections of large files
- **Pattern Matching**: Support for literal and regex pattern matching
- **Recursive Search**: Search through directories recursively
- **Case-Insensitive Search**: Optional case-insensitive pattern matching
- **Context Display**: Show surrounding lines for grep matches

### Improved

#### 🎨 Enhanced User Experience
- **Better Visual Feedback**: Clear indicators for tool execution, errors, and status
- **Improved Error Messages**: More descriptive error messages with context
- **Cleaner Output**: Reduced clutter and better formatting
- **Process Status Display**: Clear display of background process information
- **Tool Execution Feedback**: Immediate feedback when tools execute

#### ⚡ Performance Optimizations
- **Streaming Performance**: Optimized buffer management for smooth streaming
- **Tool Execution Speed**: Faster tool detection and execution
- **Memory Efficiency**: Better memory management for large outputs
- **Output Truncation**: Smart truncation of very long outputs (>10,000 chars)

#### 🔒 Stability & Reliability
- **Error Recovery**: Better error handling and recovery mechanisms
- **Graceful Degradation**: Falls back gracefully when features aren't available
- **Process Cleanup**: Proper cleanup of background processes
- **Session Management**: Improved session state management
- **Recursion Protection**: Safety limits to prevent infinite loops

### Fixed

#### 🐛 Bug Fixes
- **Mode Toggle Issue**: Fixed prompt not appearing immediately after mode switch
- **Auto-Continuation Loop**: Fixed infinite continuation loops
- **Tool Detection**: Fixed JSON tool block detection in streaming responses
- **end_response Detection**: Fixed proper detection of end_response tool calls
- **Background Process Tracking**: Fixed process ID tracking and management
- **Output Display**: Fixed output truncation and display issues
- **Error Propagation**: Fixed error handling in tool execution

#### 🔧 Technical Fixes
- **Mutable State Issue**: Fixed terminal mode state using list for mutability
- **Prompt Session Exit**: Fixed clean exit from prompt sessions during mode toggle
- **Stream Buffer Management**: Fixed buffer management in streaming responses
- **Tool Result Yielding**: Fixed immediate yielding of tool results
- **Continuation Logic**: Fixed smart continuation decision making

### Technical Details

#### Architecture Changes
- **Streaming Engine**: New `_stream_with_live_tools()` method for real-time streaming
- **Tool Execution**: New `_execute_single_tool_live()` for immediate tool execution
- **Auto-Continuation Manager**: Enhanced with smart continuation logic
- **Mode Toggle Handler**: New prompt session exit mechanism for mode switching
- **Background Process Manager**: Enhanced process tracking and management

#### New Methods & Functions
- `_stream_with_live_tools()`: Stream AI responses with live tool detection
- `_execute_single_tool_live()`: Execute tools immediately during streaming
- `should_continue()`: Smart logic to determine when to auto-continue
- `toggle_mode_handler()`: Handle Shift+Tab mode switching
- `run_async_command()`: Execute commands in background

#### Configuration Updates
- Updated system prompt with auto-continuation instructions
- Added exploratory command detection list
- Enhanced tool execution feedback messages
- Improved continuation prompt generation

### Documentation

#### New Documentation Files
- `TERMINAL_MODE.md`: Complete guide to terminal mode and mode switching
- `LIVE_RESPONSE.md`: Guide to live response streaming and tool execution
- `SMART_AUTO_CONTINUATION.md`: Documentation of smart auto-continuation system
- `CHANGELOG.md`: This changelog file

#### Updated Documentation
- `README.md`: Updated with new features and capabilities
- `pyproject.toml`: Updated URLs and metadata
- `setup.py`: Created for alternative installation method

### Dependencies

No new dependencies added. All features work with existing dependencies:
- `prompt-toolkit>=3.0.0`: For terminal mode and key bindings
- `rich>=13.0.0`: For formatted output
- `psutil>=5.9.0`: For process management
- All existing AI provider dependencies remain the same

### Breaking Changes

None. All changes are backward compatible.

### Migration Guide

No migration needed. All features work automatically:
1. **Terminal Mode**: Just press `Shift+Tab` to toggle modes
2. **Live Streaming**: Automatically enabled for all responses
3. **Smart Continuation**: Works automatically based on context
4. **Background Commands**: Use existing command_runner tool with `operation: "run_async_command"`

### Known Issues

None currently identified.

### Future Enhancements

Potential improvements for future releases:
- [ ] Configurable auto-continuation behavior
- [ ] Custom mode toggle key binding
- [ ] Process output streaming in real-time
- [ ] Enhanced grep with syntax highlighting
- [ ] File watcher for live updates
- [ ] Multi-file editing support

---

## [1.1.0] - Previous Release

Previous features and changes...

---

**Note**: This changelog documents all major features and improvements implemented after restoring from backup on November 8, 2025.
