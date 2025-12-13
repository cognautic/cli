# Changelog

All notable changes to Cognautic CLI will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.3-1] - 2025-12-12

### Added
- **Ask Question Feature** (`/askq` command)
  - AI can now proactively ask clarifying questions when confused or uncertain
  - Toggle feature on/off with `/askq on` or `/askq off`
  - AI provides 2-3 specific options plus automatic "Something else" for custom input
  - Beautiful terminal UI with Rich panels for question display
  - Mandatory scenarios where AI MUST ask questions:
    - Framework/technology not specified
    - Database/storage not specified
    - Programming language ambiguous
    - Multiple valid approaches exist
    - Styling/UI framework not clear
  - User's answer automatically injected as follow-up message to AI
  - Seamless conversation flow without manual re-prompting

### Fixed
- Auto-continuation now properly handles ask_question tool results
- User answers are automatically sent to AI as follow-up messages
- AI now correctly uses custom answers provided by users
- Added json import to fix tool execution error
- Tool result structure properly includes answer data for continuation

### Changed
- Enhanced system prompt with explicit mandatory scenarios for asking questions
- Added detailed instructions on when and how AI should ask questions
- Improved auto-continuation prompt builder to inject user answers
- Updated help documentation to include `/askq` command

---
