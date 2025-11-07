# Changelog

All notable changes to Cognautic CLI will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.1] - 2025-11-07

### Added

#### Provider & Model Persistence
- **Provider Persistence**: Last used provider is now saved to `~/.cognautic/config.json`
  - Automatically loads on startup
  - Persists across CLI restarts
  - Saved when switching providers with `/provider <name>`
- **Model Persistence**: Last used model is now saved globally and per-provider
  - Global `last_model` setting in config
  - Provider-specific model preferences
  - Automatically loads on startup

#### File Operations Improvements
- **Flexible Parameter Support**: `create_directory` now accepts both `path` and `dir_path` parameters
  - Improves compatibility with AI-generated tool calls
  - Prevents "unexpected keyword argument" errors
  - Maintains backward compatibility

### Fixed

#### Keyring Warning Suppression
- **Silent Fallback**: Removed verbose keyring initialization warning
  - No longer shows warning when keyring backend is unavailable
  - Silently falls back to no encryption
  - Cleaner startup experience
  - Changed from `console.print()` warning to silent exception handling

### Changed

#### System Prompt Simplification
- **Documentation Requirement**: Simplified web search documentation workflow
  - Removed mandatory MD folder creation requirement
  - Changed from "always create MD files" to "perform web search if project is hard"
  - Reduces unnecessary file creation
  - Streamlines development workflow

#### Configuration Management
- **Enhanced Config Methods**: Improved configuration persistence
  - `set_config()` now used for provider/model persistence
  - `get_config_value()` retrieves saved preferences
  - Better integration with startup flow

### Technical Details

#### Files Modified
- `cognautic/config.py`:
  - Suppressed keyring initialization warning
  - Silent exception handling for keyring failures
- `cognautic/cli.py`:
  - Added provider persistence on `/provider` command
  - Added model persistence on `/model` command
  - Load saved provider/model on startup
  - Updated help message from "Ctrl+X" to "Ctrl+C"
  - Updated version to 1.1.1
  - Added nested try-catch for KeyboardInterrupt during streaming
  - Saves partial responses when interrupted
- `cognautic/tools/file_operations.py`:
  - Updated `_create_directory()` to accept both `path` and `dir_path` parameters
- `cognautic/ai_engine.py`:
  - Simplified system prompt documentation requirements
- `cognautic/__init__.py` - **NEW**: Package metadata (version 1.1.1)
- `pyproject.toml` - **NEW**: Modern Python packaging configuration
- `setup.py` - **NEW**: Setuptools configuration

#### Configuration Schema
```json
{
  "last_provider": "openrouter",
  "last_model": "openai/gpt-4o-mini",
  "providers": {
    "openrouter": {
      "model": "openai/gpt-4o-mini"
    }
  }
}
```

### User Experience Improvements

1. **Persistent Preferences**: Provider and model choices remembered across sessions
2. **Stop Control**: Can stop long AI responses with Ctrl+C without exiting chat
3. **Cleaner Output**: No keyring warnings on startup
4. **Better Error Handling**: Fixed directory creation parameter errors
5. **Flexible Workflows**: Simplified documentation requirements for faster development

### Breaking Changes
None - All changes are backward compatible.

### Migration Guide
No migration needed. Existing configurations will work as-is. New features are automatically enabled.

---
