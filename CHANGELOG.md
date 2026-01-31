# Changelog

All notable changes to Cognautic CLI will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.4] - 2026-01-31

### Added
- **Native Tool Support Improvements**
  - Migrated Google provider to the new `google-genai` SDK for better performance and future-proofing.
  - Implemented full support for Gemini `thought_signatures`, enabling stable parallel tool calls.
  - Added binary data handling in the session memory system to securely persist tool call metadata.

### Fixed
- **Gemini Stability Fixes**
  - Resolved `400 Bad Request` errors related to tool turn order and missing signatures.
  - Fixed `TypeError: Object of type bytes is not JSON serializable` during session saves.
  - Corrected streaming issues where async iterators were not properly awaited.

### Changed
- **Refined Agentic Workflow**
  - **Removed Continue Prompts**: The CLI now uses a recursive execution model that handles multi-step tool sequences automatically without requiring manual "continue" confirmations.
  - **Eager Tool Execution**: Tools detected during streaming are executed immediately to provide faster feedback and a smoother user experience.
  - Updated dependencies to use `google-genai>=0.1.0`.

---
