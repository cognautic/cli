# Changelog

All notable changes to Cognautic CLI will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.4-5] - 2026-02-27

### Added
- **Response Control**
  - Added `Esc` key support to stop active AI streaming responses in chat mode.

### Fixed
- **Google Gemini Tool Calling**
  - Fixed missing `thought_signature` propagation by attaching signatures to all replayed function-call parts in a tool-call turn.
  - Added history repair for malformed Gemini turns (missing signatures and out-of-order function-call turns) to avoid 400 `INVALID_ARGUMENT` errors.

### Removed
- **Debug Logging**
  - Removed noisy streaming debug output (`DEBUG: Yielding tool ... with signature`).

---

## [1.2.4-4] - 2026-02-19

### Removed
- **DEBUG Prints**
  -Removed DEBUG: Captured signature from part.
### Fixed Telemetry
  -Fixed Telemetry.
---
