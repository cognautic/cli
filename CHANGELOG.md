# Changelog

All notable changes to Cognautic CLI will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.3] - 2025-11-08

### Fixed

#### 🐛 Critical Bug Fixes
- **Auto-Continuation Not Working**: Fixed critical bug where auto-continuation would show "🔄 Auto-continuing..." but then stop without actually continuing
  - **Root cause**: Continuation prompt was being generated but not added to the message history
  - **Solution**: Now properly adds continuation prompt to messages before recursive streaming
  - **Impact**: Auto-continuation now works correctly after exploratory commands (ls, pwd, etc.)

#### > Terminal Mode Improvements
- **Live Command Output**: Terminal mode now shows command output in real-time as it's generated
  - Changed from `subprocess.run()` with buffered output to `subprocess.Popen()` with streaming
  - Line-by-line output display for better user experience
  - Real-time progress indicators for long-running commands (npm install, pip install, etc.)

### Technical Details

#### Changes to `ai_engine.py`
- Modified auto-continuation logic in `_stream_with_live_tools()`:
  - Removed unused `generate_continuation()` call that was generating but discarding the prompt
  - Now directly calls `build_continuation_prompt()` to get the continuation message
  - Properly appends continuation prompt to messages list before recursive call
  - Ensures AI receives the continuation context to actually continue the task

#### Changes to `cli.py`
- Replaced `subprocess.run()` with `subprocess.Popen()` in terminal mode
- Added real-time stdout/stderr streaming with `readline()`
- Implemented line-buffered output (`bufsize=1`) for immediate display
- Added KeyboardInterrupt handler for Ctrl+C support
- Process termination with 2-second timeout and fallback to force kill
- Removed unnecessary directory changes (already handled by `cwd` parameter)

### Impact

**Auto-Continuation Before:**
```
You: add different maps
AI: [Runs ls -la]
🔄 Auto-continuing...
You:  [Stops - no continuation, prompt returns]
```

**Auto-Continuation After:**
```
You: add different maps
AI: [Runs ls -la]
🔄 Auto-continuing...
AI: [Reads main.py file]
AI: [Creates new map files]
AI: [Updates code]
✅ Response Completed
```

**Terminal Mode Before:**
```
🖥️  You: npm install
[Wait 45 seconds with no output...]
[Finally shows all output at once]
added 1432 packages in 45s
```

**Terminal Mode After:**
```
>  You: npm install
added 1 package in 0.5s
added 5 packages in 1.2s
added 15 packages in 2.8s
added 50 packages in 8.1s
...
added 1432 packages in 45s
[Output streams line-by-line in real-time]
```

### Added
- **Session Loading by Index**: Can now load sessions using index numbers from `/session list` instead of full session IDs
  - `/session list` now shows numbered indices: `[1] session-id - title`
  - `/session load 1` loads the first session in the list
  - `/session load <id>` still works with full session IDs
  - Automatic detection: numeric input = index, alphanumeric = session ID

### Changed
- **Tool Display Improvements**:
  - Removed all emojis from tool execution boxes (🔧, ✅, ❌, etc.)
  - Removed file content previews after tool execution
  - Moved diffs inside tool boxes instead of displaying them separately
  - Removed ANSI color codes from diffs (now plain `+` and `-` markers)
  - Tool boxes now show output previews directly:
    - Command output: First 10 lines
    - File reads: First 5 lines of content
    - File writes: Complete unified diff
  - Improved box border alignment with proper truncation for long lines

- **Better Continuation Context**: Tool results now include actual data for AI continuation
  - File operations include file path and modification status
  - File reads include content preview (first 500 chars)
  - Commands include full output
  - Fixes issue where AI would say "output was not relayed back to me"

### Fixed
- **Tool Box Border Alignment**: Fixed misaligned borders when content lines were too long
  - Now properly truncates long lines with "..." suffix
  - Handles ANSI color codes correctly during truncation
  - All borders now align perfectly at 65 character width

---

