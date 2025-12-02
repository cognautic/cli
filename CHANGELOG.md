# Changelog

All notable changes to Cognautic CLI will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.1] - 2025-12-02

### Added - Repository Documenter 📚

**Native Git Repository Documentation Generator**

Added a built-in feature to automatically generate comprehensive documentation for any public git repository using AI.

#### Key Features

- **One-Command Documentation** - Generate complete documentation with a single command
- **AI-Powered Analysis** - Analyzes repository structure, code, and configuration files
- **Architecture Diagrams** - Automatically generates Python scripts for creating architecture diagrams using Graphviz
- **Comprehensive Output** - Includes project overview, installation instructions, usage guide, code structure, and architecture description
- **Smart File Selection** - Intelligently selects key files (README, package.json, requirements.txt, source files, etc.)
- **Automatic Cleanup** - Cleans up temporary cloned repositories after analysis

#### Usage

```bash
/docrepo <git_url>
```

**Example:**
```bash
/docrepo https://github.com/user/awesome-project
```

#### Output Files

The command generates two files in your current workspace:
1. `{repo_name}_DOCS.md` - Comprehensive documentation in Markdown format
2. `extra/{repo_name}_graph.py` - Python script to generate architecture diagram (requires graphviz)

#### Technical Details

- **Module:** `cognautic/repo_documenter.py`
- **Command:** `/docrepo` integrated into CLI slash commands
- **Shallow Clone:** Uses `git clone --depth 1` for faster cloning
- **Token Optimization:** Limits file contents to prevent context overflow
- **File Size Limits:** Only reads source files under 15KB
- **Supported Languages:** Python, JavaScript, TypeScript, Rust, Go, Java, C/C++, Ruby, PHP, Vue, Swift, Kotlin, Scala, C#
- **File Creation:** AI uses its `write_to_file` tool to create documentation files (prevents duplication)

---