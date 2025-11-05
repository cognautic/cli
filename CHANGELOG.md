# Changelog

All notable changes to Cognautic CLI will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.1.0] - 2025-11-05

### Added

#### Rules Management System

**Global and Workspace Rules** - A powerful new feature that allows you to define custom rules for AI behavior at both global and workspace levels.

#### Intelligent Web Search Before Implementation

**Automatic Web Research** - The AI now automatically searches the web before implementing features that require current or external information, ensuring up-to-date implementations with latest best practices and API documentation.

#### Features

- **Global Rules**: Define rules that apply across all workspaces and sessions
  - Stored in `~/.cognautic/global_rules.json`
  - Persistent across all projects
  - Perfect for coding standards, preferences, and general guidelines

- **Workspace Rules**: Define rules specific to individual projects
  - Stored in `.cognautic_rules.json` in the workspace directory
  - Project-specific conventions and requirements
  - Can override or complement global rules

#### Commands

All rules commands are available in chat mode using the `/rules` or `/rule` prefix:

```bash
# Display all rules (global and workspace)
/rules

# Add a global rule
/rules add global <rule_text> [optional description]

# Add a workspace rule
/rules add workspace <rule_text> [optional description]

# Remove a rule by index
/rules remove global <index>
/rules remove workspace <index>

# Clear all rules of a type
/rules clear global
/rules clear workspace
```

#### Usage Examples

**Adding Global Rules:**
```bash
/rules add global Always use type hints in Python code [Improves code quality]
/rules add global Follow PEP 8 style guidelines
/rules add global Write docstrings for all functions
```

**Adding Workspace Rules:**
```bash
/rules add workspace Use React hooks instead of class components
/rules add workspace All API endpoints must include error handling
/rules add workspace Follow the existing project structure in src/
```

**Viewing Rules:**
```bash
/rules
```

This displays a formatted table showing:
- All global rules with their descriptions
- All workspace rules for the current workspace
- Index numbers for easy removal

**Removing Rules:**
```bash
/rules remove global 0    # Remove first global rule
/rules remove workspace 2 # Remove third workspace rule
```

**Clearing Rules:**
```bash
/rules clear global      # Remove all global rules
/rules clear workspace   # Remove all workspace rules
```

#### How It Works

1. **Rule Storage**:
   - Global rules: `~/.cognautic/global_rules.json`
   - Workspace rules: `<workspace>/.cognautic_rules.json`

2. **Rule Application**:
   - Rules are automatically loaded when you start a chat session
   - Both global and workspace rules are provided to the AI as context
   - The AI follows these rules when generating responses and code

3. **Rule Format**:
   Each rule is stored as a JSON object with:
   - `rule`: The rule text
   - `description`: Optional description for context
   - `type`: Either "global" or "workspace"

#### Benefits

✅ **Consistency**: Ensure AI follows your coding standards across all sessions
✅ **Project-Specific**: Define rules unique to each project
✅ **Flexibility**: Combine global and workspace rules for maximum control
✅ **Persistence**: Rules are saved and automatically applied
✅ **Easy Management**: Simple commands to add, remove, and view rules

#### Technical Details

- **New Module**: `cognautic/rules.py` - Complete rules management system
- **CLI Integration**: Rules commands integrated into chat mode
- **Storage Format**: JSON for easy editing and portability
- **Workspace Detection**: Automatically detects current workspace
- **Rich Display**: Formatted tables for easy viewing

#### File Structure

**Linux/macOS:**
```
~/.cognautic/
├── global_rules.json          # Global rules (all workspaces)
└── config.json                # Existing config

<workspace>/
└── .cognautic_rules.json      # Workspace-specific rules
```

**Windows:**
```
C:\Users\<YourUsername>\.cognautic\
├── global_rules.json          # Global rules (all workspaces)
└── config.json                # Existing config

<workspace>\
└── .cognautic_rules.json      # Workspace-specific rules
```

**File Locations:**
- **Linux/macOS**: `~/.cognautic/global_rules.json` (e.g., `/home/username/.cognautic/global_rules.json`)
- **Windows**: `C:\Users\<YourUsername>\.cognautic\global_rules.json`
- **Workspace Rules**: `.cognautic_rules.json` in your project directory (all platforms)

---

### Changed

- **Help Command**: Updated `/help` to include detailed rules management subcommands
- **CLI Module**: Enhanced `cli.py` with rules command handler and standalone `cognautic rules` command
- **AI Engine**: Integrated rules into system prompt - AI now receives and follows user-defined rules
- **Project Structure**: Cleaned up unnecessary documentation files

### Removed

- Removed obsolete changelog files:
  - `CONTEXT_WINDOW_FIX.md`
  - `GGUF_PERFORMANCE_OPTIMIZATION.md`
  - `GGUF_SUPPORT_ADDED.md`
  - `LOCAL_PROVIDER_FIX.md`
  - `PERSISTENT_MODEL_SELECTION.md`
- Removed `MD/` directory with redundant documentation
- Removed `next-to-fix.txt` development file
- Removed development and testing directories:
  - `docs/` - Documentation folder
  - `scripts/` - Installation scripts
  - `test/` - Test directory
  - `tests/` - Test suite
- Cleaned up build artifacts (`build/`, `dist/`, `*.egg-info/`, `__pycache__/`)

### Developer Notes

**New Files:**
- `cognautic/rules.py` - Rules management system

**Modified Files:**
- `cognautic/cli.py` - Added rules command handler and help text

**API Changes:**
- New `RulesManager` class with methods:
  - `add_global_rule(rule, description)`
  - `add_workspace_rule(rule, description, workspace_path)`
  - `remove_global_rule(index)`
  - `remove_workspace_rule(index, workspace_path)`
  - `list_global_rules()`
  - `list_workspace_rules(workspace_path)`
  - `get_all_rules(workspace_path)`
  - `get_rules_for_ai(workspace_path)`
  - `display_rules(workspace_path)`
  - `clear_global_rules()`
  - `clear_workspace_rules(workspace_path)`

---

## Migration Guide

### For Existing Users

No migration needed! The rules system is entirely new and doesn't affect existing functionality.

To start using rules:

1. **Add your first global rule:**
   ```bash
   cognautic chat
   /rules add global Always write clean, maintainable code
   ```

2. **Add workspace rules for your project:**
   ```bash
   /workspace ~/my-project
   /rules add workspace Use TypeScript for all new files
   ```

3. **View your rules anytime:**
   ```bash
   /rules
   ```

### For Developers

If you're integrating with Cognautic CLI:

```python
from cognautic.rules import RulesManager

# Initialize rules manager
rules_manager = RulesManager()

# Get rules for AI context
rules_text = rules_manager.get_rules_for_ai(workspace_path="/path/to/project")

# Add to your AI prompt
prompt = f"{user_message}\n\nRules to follow:\n{rules_text}"
```

---

## Future Enhancements

Planned improvements for the rules system:

- [ ] Rule templates for common frameworks (React, Django, etc.)
- [ ] Import/export rules between workspaces
- [ ] Rule categories and tags
- [ ] Rule priority levels
- [ ] Conditional rules based on file types
- [ ] Rule validation and suggestions
- [ ] Shared team rules via Git

---

## Support

For questions or issues with the rules system:
- Email: cognautic@gmail.com
- Documentation: See README.md for complete usage guide

---

**Full Changelog**: v1.1.0...v1.1.0
