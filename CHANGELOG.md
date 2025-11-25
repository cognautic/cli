# Changelog

All notable changes to Cognautic CLI will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.10-2] - 2025-11-25

### Added - Restricted Directory Protection 🛡️

**Safety Feature: Prevent Running in Sensitive Directories**

This update adds protection to prevent users from accidentally running Cognautic CLI in restricted system directories where it could cause unintended modifications.

#### What Was Added

- **Restricted Directory Validation** - CLI now blocks execution in sensitive directories:
  - **Home Directory** - Cannot run in user home directory (Linux/Mac: `~`, Windows: `C:\Users\username`)
  - **System Directories** - Cannot run in `/man` directory on Linux/Unix systems
  - **Drive Root** - Cannot run in `C:\` drive root on Windows
  
- **Dual Validation Points**:
  1. **Startup Validation** - Checks workspace when CLI starts
  2. **Workspace Change Validation** - Checks when using `/workspace` or `/ws` commands

#### Technical Implementation

- **File Modified:** `cognautic/utils.py`
  - Added `is_restricted_directory()` function
  - Cross-platform support (Linux, macOS, Windows)
  - Returns tuple of (is_restricted: bool, reason: Optional[str])
  - Handles path resolution and edge cases gracefully

- **File Modified:** `cognautic/cli.py`
  - Added import for `is_restricted_directory` from utils
  - Validation on initial workspace setup (line ~395)
  - Validation on workspace change via slash commands (line ~1067)
  - Clear error messages guide users to proper directories

#### User Experience

**Before (No Protection):**
```bash
$ cd ~
$ cognautic
# Would start in home directory - risky!
```

**After (Protected):**
```bash
$ cd ~
$ cognautic
ERROR: Cannot run Cognautic CLI in your home directory (/home/username). 
       Please navigate to a specific project directory.
INFO: Please navigate to a specific project directory and try again.
Chat session ended

$ cd ~/my-project
$ cognautic
# Works normally in project directory ✓
```

**Workspace Change Protection:**
```
You: /workspace ~
ERROR: Cannot run Cognautic CLI in your home directory (/home/username).
       Please navigate to a specific project directory.
INFO: Please choose a specific project directory.
```

#### Benefits

- ✅ **Prevents Accidental File Creation** - No more files created in home directory
- ✅ **Protects System Directories** - Blocks dangerous operations in `/man` and `C:\`
- ✅ **Clear Error Messages** - Users know exactly why and what to do
- ✅ **Cross-Platform** - Works on Linux, macOS, and Windows
- ✅ **Non-Breaking** - Only affects restricted directories, normal usage unaffected

#### Files Modified

- `cognautic/utils.py` - Added `is_restricted_directory()` validation function
- `cognautic/cli.py` - Added validation checks at startup and workspace changes

#### Testing

Tested on Linux:
- ✅ Blocks execution in home directory (`/home/username`)
- ✅ Blocks execution in `/man` directory
- ✅ Allows execution in subdirectories (`/home/username/projects`)
- ✅ Blocks workspace change to restricted directories via `/ws` command
- ✅ Proper error messages displayed

---
