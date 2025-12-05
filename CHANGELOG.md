# Changelog

All notable changes to Cognautic CLI will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.2] - 2024-12-05

### Added
- **Multi-Agent Collaboration Mode** (`/multiagent` command)
  - Enable multiple AI models to collaborate on projects through structured phases
  - Three-phase workflow: Discussion → Planning → Execution
  - Side-by-side split-screen view during execution phase
  - Real-time streaming output from all agents working in parallel
  - Shared workspace for seamless integration
  - Automatic YOLO mode activation for smooth collaboration
  - Support for any combination of providers (OpenAI, Anthropic, Google, OpenRouter, Groq, etc.)
  
- **Improved Setup UX**
  - Numbered menu system for provider configuration (select by 1-2-3-4-5 instead of y/n)
  - Shows configuration status for each provider (✓ Configured / Not configured)
  - Direct links to API key pages for each provider
  - Configure providers in any order
  - Set default provider from numbered list
  - Added support for more providers: Groq, Mistral, DeepSeek

### Fixed
- Provider reinitialization before multiagent validation to pick up newly configured providers
- Tool usage prevention in discussion and planning phases (agents now only discuss, not execute)
- Execution phase now prevents agents from calling `end_response` prematurely
- Improved error messages showing available vs configured providers

### Changed
- Multi-agent execution now uses shared workspace instead of separate folders per agent
- Discussion and planning phases now call providers directly to avoid tool system activation
- Enhanced prompts to explicitly prevent tool usage during non-execution phases

---