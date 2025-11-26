# Changelog

All notable changes to Cognautic CLI will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.10-3] - 2025-11-26

### Fixed - Web Search Tool Integration 🔍

**Restored Web Search Functionality in Auto-Continuation**

This update fixes a critical issue where web search results were not being correctly passed to the AI's context during auto-continuation, causing the AI to believe no results were found.

#### What Was Fixed

- **Web Search Result Handling** - The `ai_engine` now correctly identifies and structures `web_search` tool results instead of treating them as generic tool outputs.
- **Auto-Continuation Context** - The `auto_continuation` module now explicitly formats and includes web search hits (titles, URLs, snippets) in the prompt sent back to the AI.

#### Technical Implementation

- **File Modified:** `cognautic/ai_engine.py`
  - Added specific handler for `web_search` in `_execute_single_tool_live`.
  - Ensures results are saved with `type: "web_search"` and full data payload.
  
- **File Modified:** `cognautic/auto_continuation.py`
  - Added logic to `generate_continuation` to parse `web_search` results.
  - Formats search results into a readable "WEB SEARCH RESULTS" block for the AI.

#### User Experience

**Before:**
The AI would perform a search, but in the next step would say "It seems the previous web search did not yield results" because it couldn't see the output.

**After:**
The AI successfully sees the search results and uses the information to answer questions or generate code.

---
