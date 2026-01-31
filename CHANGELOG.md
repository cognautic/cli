# Changelog

All notable changes to Cognautic CLI will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.4-1-1] - 2026-01-31

### Fixed
- **Google Provider Critical Hotfix**
  - Implemented robust `thought_signature` capture to prevent 400 errors with Gemini models.
  - Added self-healing history sanitization to repair "orphan" function responses in existing sessions.
  - Fixed silent failures in `Part` creation that led to dropped function calls.
---
