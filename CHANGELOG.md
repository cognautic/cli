# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [1.1.9] - 2025-11-19
### Added
- Voice input for prompts.
  - Ctrl+G: One-shot capture to prefill the next prompt.
  - `/voice`: Slash command to record once and prefill.
- Vim editor integration.
  - `/editor [filepath]`: Open vim editor directly from chat.
  - Ctrl+E in vim: Save changes and return to chat.
  - Supports both absolute and relative file paths.


### Changed
- Prompt hint updated to include Ctrl+G voice input shortcut.

### Fixed
- Suppressed ALSA/libportaudio stderr noise during microphone initialization and recording.

### Dependencies
- Optional extras for voice input: `SpeechRecognition` and `PyAudio` under the `voice` extra.
  - Install with: `pip install -e .[voice]` or `pip install SpeechRecognition PyAudio`

---