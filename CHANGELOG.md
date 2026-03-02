# Changelog

All notable changes to Cognautic CLI will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.5] - 2026-03-02

### Added
- Interactive `/config` menu with direct actions, including:
  - set API key for provider
  - set `custom_openai` base URL
  - list all supported providers with status
- New `custom_openai` provider (OpenAI-compatible API type).

### Changed
- Simplified terminal UI output and startup/help presentation.
- Re-added community links (Discord/Instagram) in a boxed section.
- Replaced tool output box rendering with plain text.
- Added file diff display for file content-changing operations.
- Confirmation flow now uses explicit blocking `y/n` accept/reject prompts.
- ESC is reserved for stopping active AI response streaming.
- Added spinner while AI is processing responses.
- `/model` now fetches models for the current provider when used without arguments.
- Provider switching now reinitializes configured providers when needed.
- Improved completion menu styling controls for visibility.

### Removed
- Removed `response_control` tool and related runtime handling.

## [1.2.4-5] - 2026-03-01

### Added
- **Contact**
  -Added Discord and Instagram Contacts.

---
