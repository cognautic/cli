# Changelog

All notable changes to Cognautic CLI are documented in this file.

The format is based on Keep a Changelog, and this project adheres to Semantic Versioning.

## [1.1.7] - 2025-11-14

### Added
- Ollama provider integration (no API key required)
  - New provider `ollama` with default base URL `http://localhost:11434/api`
  - Endpoints: `POST /chat`, `GET /tags` for models
  - Works with `/provider ollama`
  - New `/endpoint` command to set per-provider base URL override (e.g., remote host)
  - `/model list` supports Ollama via `/api/tags`
  - Documentation: added `OLLAMA.md` guide (setup, endpoint override, examples, troubleshooting)
- Multi-Model Testing Mode (side-by-side)
  - New `/mml` command enables parallel testing with multiple AI models
  - Each model runs in its own isolated folder to avoid conflicts
  - Automatic YOLO mode activation for seamless multi-model operation
  - Live, per-model streaming using Rich Live + Columns; each model starts immediately
  - Threaded producers + async consumers to guarantee concurrency even with blocking SDKs
  - One final static snapshot after completion for scrollback
  - Example: `/mml google gemini-2.5-flash openrouter gpt-4`
- Folder name sanitization for models with special characters (`:`, `/`, `\`, etc.)
- Graceful error handling for folder creation failures in multi-model mode

### Changed
- Startup provider selection and validation
  - The CLI now combines configured providers (with API keys) and no-auth providers (e.g., Ollama)
  - API key is only enforced for providers that actually require it
  - If a selected provider lacks a required API key, the CLI falls back to a valid provider instead of aborting
- Multi-model layout and UX
  - Fixed column widths to prevent layout shifts during streaming
  - Wrapped content inside panels to avoid horizontal overflow
  - Folder creation now uses `parents=True` for better reliability
  - Error messages for folder creation are warnings to allow partial success
  - Enhanced validation ensures at least one model folder is created before enabling multi-model mode

### Fixed
- Provider registry boolean literal for `ollama` (`true` -> `True`) to prevent import error
- Startup error "No API key found for ollama" by honoring no-auth providers and adding fallback
- `UnboundLocalError` from local `threading` import shadowing; rely on module-level import
- Multi-model runs no longer wait for the first model to finish; all start together
- Removed periodic snapshot printing that caused duplicate boxes and scroll issues

