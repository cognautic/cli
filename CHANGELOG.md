# Changelog

All notable changes to Cognautic CLI will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.5] - 2025-11-11

### 🎉 Major Fixes

#### Fixed File Content Not Being Sent to AI
- **Issue**: When AI used `read_file` tool, it would execute successfully and show tool boxes, but the actual file content was never sent to the AI in continuation messages
- **Impact**: AI would guess what was in files instead of analyzing actual content, leading to incorrect responses
- **Root Cause**: Main streaming path in `ai_engine.py` was setting incorrect type (`file_op` instead of `file_read`) and not including content field in `tool_results`
- **Solution**: 
  - Separated read operations from other file operations in main streaming path
  - Extract file content and add to `tool_results` with correct type `file_read`
  - Inject file content into system prompt for continuation (works with all providers, especially Google)
  - Use prominent headers (`======`) to ensure content is visible in flattened prompts

#### Implemented True Real-Time Streaming
- **Issue**: Responses were buffered and displayed with artificial delays instead of showing tokens immediately as they arrived from provider servers
- **Impact**: Poor user experience with delayed responses that felt sluggish and unresponsive
- **Root Causes**:
  - 10-character buffer in `_stream_with_live_tools` delayed token display
  - Artificial typing delay in CLI slowed down output character-by-character
  - Google provider's synchronous iteration blocked the async event loop
  - OpenRouter, OpenAI, Anthropic, and Together providers lacked streaming support
- **Solution**:
  - Removed 10-character buffer - tokens now yield immediately as received
  - Removed artificial typing delays and character-by-character iteration
  - Added `await asyncio.sleep(0)` to Google provider to prevent event loop blocking
  - Added `generate_response_stream()` method to all providers (OpenAI, Anthropic, Together, OpenRouter)
  - Improved JSON sanitization to handle control characters in tool calls

#### Fixed JSON Parsing Errors in Tool Calls
- **Issue**: Multiple JSON parse warnings when AI included newlines or control characters in string values
- **Impact**: Tool execution would fail with repeated error messages
- **Solution**: Added automatic JSON sanitization that escapes newlines, carriage returns, and tabs in string values before parsing

#### Fixed Spaces Being Stripped During Streaming
- **Issue**: AI responses appeared without spaces between words (e.g., "I'llhelpyoubuild" instead of "I'll help you build")
- **Impact**: All streamed responses were unreadable, especially from OpenRouter models
- **Root Cause**: `_clean_model_syntax()` was calling `.strip()` on each chunk, removing trailing spaces that separate words
- **Solution**: Removed `.strip()` call to preserve whitespace during streaming while still cleaning model syntax tokens

#### Fixed OpenRouter Models Not Executing Tools
- **Issue**: OpenRouter models (e.g., `z-ai/glm-4.5-air:free`, `openai/gpt-oss-20b:free`, `kwaipilot/kat-coder-pro:free`) were not executing tools despite outputting JSON
- **Impact**: Tools like `web_search` and `file_operations` would not run, only JSON would be displayed
- **Root Causes**:
  - JSON blocks were being yielded as text before detection could occur
  - Streaming was too fast, entire JSON blocks appeared before pattern matching
  - Models output raw JSON without markdown code fences (` ```json ... ``` `)
  - Some models output incomplete JSON (missing closing braces)
- **Solution**: 
  - Implemented smart buffering to prevent premature yielding of JSON blocks
  - Keep 10-character buffer at end of text to catch JSON markers
  - Detect partial JSON markers (` ``` `, `{`, `{"tool`) and hold text
  - Made regex patterns more flexible (match ` ```json ` without requiring newline)
  - Added flexible pattern matching for raw JSON with optional prefixes
  - Implemented brace counting to find complete JSON objects
  - Added auto-closing for incomplete JSON at end of stream
  - Handles both code-fenced and raw JSON formats universally
- **Result**: ✅ All OpenRouter models now execute tools correctly

#### Fixed Tool Operation Errors
- **Issue**: AI models were calling operations on wrong tools (e.g., calling `read_file_lines` on `file_reader` instead of `file_operations`)
- **Impact**: Tools failed with "Unknown operation" errors, breaking file operations
- **Root Cause**: System prompt didn't clearly specify which operations belong to which tool
- **Solution**: 
  - Added comprehensive "AVAILABLE TOOLS AND THEIR OPERATIONS" section in system prompt
  - Clearly documented that `file_operations` has all read/write operations
  - Specified that `file_reader` is rarely needed and only for advanced grep searches
  - Added explicit instruction: "ALWAYS use 'file_operations' tool for reading/writing files, NOT 'file_reader'"
- **Result**: ✅ AI now calls correct tools with correct operations

### Added

- **File Content in System Prompt**: File content is now automatically injected into the system prompt during auto-continuation, ensuring all AI providers (especially Google Gemini with its flattened prompt format) receive the actual file content
- **Session Creation Message**: Added success message when creating new session with `/session new` command
- **Content Preview in Tool Boxes**: File read operations now show a preview of file content (first 10 lines) in the tool box display
- **Async Command Instructions**: Added critical instructions in system prompt for running long-running commands (npm install, npm start, etc.) in background using `run_async_command` operation
- **Tool Operations Clarification**: Added comprehensive documentation of which operations belong to which tool to prevent AI from calling wrong tools

### Changed

- **Streaming Performance**: Completely overhauled streaming implementation for instant token display
  - Removed 10-character buffer that delayed output
  - Removed artificial typing delays (typing_speed configuration no longer needed)
  - All providers now support true real-time streaming
- **Tool Result Types**: File read operations now correctly use type `file_read` instead of generic `file_op`
- **Tool Results Structure**: Read operations now include full `content` field in `tool_results` for AI continuation
- **Version Bumped**: Updated version from 1.1.4 to 1.1.5 in `cli.py` and `PKG-INFO`
- **UI Consistency**: Changed emoji-based info messages to `INFO:` prefix for consistency
  - `📚 Codebase indexed` → `INFO: Codebase indexed`
  - `📚 Codebase Index Status` → `INFO: Codebase Index Status`

### Fixed

- **File Content Not Reaching AI**: Fixed critical bug where file content from `read_file` operations was not being passed to AI in continuation
- **Real-Time Streaming**: Fixed buffered responses - tokens now display immediately as they arrive from provider servers
- **Spaces Stripped During Streaming**: Fixed critical bug where spaces between words were removed during streaming, making responses unreadable
- **OpenRouter Tool Execution**: Fixed OpenRouter models not executing tools due to raw JSON format (without code fences)
- **Google Provider Blocking**: Fixed synchronous iteration that blocked async event loop during streaming
- **JSON Parse Errors**: Fixed repeated JSON parse warnings by automatically sanitizing control characters in tool calls
- **Google Provider Compatibility**: Improved compatibility with Google Gemini provider by injecting file content into system prompt (which is always included in flattened prompts)
- **Auto-Continuation for File Reads**: Ensured auto-continuation properly triggers and includes file content when files are read
- **Tool Box Display**: File operations now show proper content preview in tool boxes

### Removed

- **Debug Output**: Removed all temporary debug messages that were added during troubleshooting
- **Documentation Files**: Cleaned up temporary documentation and test files created during development

### Technical Details

#### Files Modified

1. **`cognautic/ai_engine.py`**
   - Lines 1195-1225: Added logic to separate read operations from other file operations
   - Lines 1196-1225: Extract file content and add to `tool_results` with type `file_read` and full content
   - Lines 977-995: Inject file content into system prompt for continuation
   - Lines 903-909: Removed 10-character buffer for immediate token yielding
   - Lines 240-254: Added `await asyncio.sleep(0)` to Google provider for non-blocking streaming
   - Lines 103-119: Added streaming support to OpenAI provider
   - Lines 164-189: Added streaming support to Anthropic provider
   - Lines 347-366: Added streaming support to Together provider
   - Lines 339-355: Added streaming support to OpenRouter provider
   - Lines 976-1004: Added raw JSON detection for OpenRouter models (without code fences)
   - Lines 1016-1086: Added brace counting to extract complete raw JSON objects
   - Lines 1008-1037: Improved JSON sanitization for tool calls with control characters
   - Line 1536-1537: Removed `.strip()` from `_clean_model_syntax()` to preserve spaces during streaming
   - Removed debug output from lines 974-977, 1001, 1587

2. **`cognautic/cli.py`**
   - Lines 439-458: Removed typing delay logic and character-by-character iteration
   - Lines 456-458: Display chunks immediately without artificial delays
   - Lines 956-960: Added success message for `/session new` command
   - Line 79: Updated version to 1.1.5
   - Lines 227, 229, 1237: Changed emoji-based messages to `INFO:` prefix

3. **`cognautic_cli.egg-info/PKG-INFO`**
   - Line 3: Updated version to 1.1.5

#### Code Changes

**Before (Broken):**
```python
# All file operations used generic type
tool_results.append({
    "type": "file_op",  # Wrong!
    "operation": operation,
    "file_path": file_path,
    "success": True,
    # No content field!
})
```

**After (Fixed):**
```python
# Read operations now handled separately
if operation in ["read_file", "read_file_lines"]:
    file_content = result.data.get("content", "")
    
    tool_results.append({
        "type": "file_read",  # Correct type!
        "file_path": file_path,
        "content": file_content,  # Full content included!
        "success": True,
    })
    
    # Inject into system prompt for continuation
    file_contents_section += f"FILE CONTENT: {file_path}\n"
    file_contents_section += f"{'='*70}\n{content}\n{'='*70}\n"
```

### Testing

Verified with the following test case:
```bash
$ cognautic chat
You: read test/src/App.js and tell me what type of app this is
```

**Expected Result**: ✅ AI correctly identifies app type based on actual file content  
**Before Fix**: ❌ AI guessed incorrectly (e.g., called Pomodoro app a "React app" or "To-Do list")  
**After Fix**: ✅ AI correctly identifies as "Pomodoro Clock application" based on actual code

### Notes

- This fix is critical for AI's ability to accurately analyze codebases
- Works with all AI providers (Google, OpenRouter, OpenAI, etc.)
- System prompt injection ensures compatibility with providers that flatten message history
- No breaking changes to existing functionality

---