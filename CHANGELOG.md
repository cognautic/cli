# Changelog

All notable changes to Cognautic CLI will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.10] - 2025-11-23

### Added
- **MCP (Model Context Protocol) Support** - Major new feature
  - Connect to external MCP servers to access their tools, resources, and prompts
  - Expose Cognautic's capabilities as an MCP server for other clients
  - Full JSON-RPC 2.0 protocol implementation
  - STDIO transport support for local MCP servers
  - HTTP/SSE transport framework (ready for implementation)
  - Automatic capability discovery (tools, resources, prompts)
  - Pre-configured servers: filesystem, GitHub, PostgreSQL
  - MCP configuration management via `~/.cognautic/mcp_servers.json`
  - New slash commands:
    - `/mcp` - Show MCP help
    - `/mcp list` - List connected servers
    - `/mcp connect <server>` - Connect to a server
    - `/mcp disconnect <server>` - Disconnect from a server
    - `/mcp tools` - List available tools
    - `/mcp resources` - List available resources
    - `/mcp config` - Show configuration
  - Comprehensive documentation:
    - `MCP_SUPPORT.md` - Full guide with architecture and troubleshooting
    - `MCP_QUICK_REFERENCE.md` - Quick start and common commands
    - `MCP_IMPLEMENTATION_SUMMARY.md` - Technical implementation details
  - Example code in `examples/mcp_example.py`

### Changed
- Updated `pyproject.toml` to include `mcp>=0.1.0` dependency
- Enhanced slash command autocomplete with MCP commands
- Updated README.md with MCP support section
- Updated cognautic-cli.html documentation with MCP section

### Documentation
- Added comprehensive MCP documentation
- Updated features list to highlight MCP support
- Added MCP to table of contents in HTML documentation
- Created example scripts demonstrating MCP usage

## [1.1.10] - 2025-11-19

### Added
- Voice input support with one-shot speech-to-text
- Vim editor integration with `/editor` command
- Ctrl+E shortcut in vim to save and return to chat
- Multi-line input support with Alt+Enter
- Background process management with `/ps` and `/ct`

### Changed
- Improved command execution with live output streaming
- Enhanced terminal mode with better process control
- Updated documentation for new features

## [1.1.8] - 2025-11-15

### Added
- Multi-model testing with `/mml` command
- Side-by-side model comparison
- Intelligent web search integration
- Codebase indexing with `/index` command

### Changed
- Improved AI response streaming
- Enhanced confirmation manager
- Better error handling

## [1.1.7] - 2025-11-10

### Added
- Local model support for Hugging Face models
- `/lmodel` command to load local models
- Ollama integration
- Model listing from provider APIs

### Changed
- Improved provider management
- Enhanced model switching
- Better API key handling

## [1.1.6] - 2025-11-05

### Added
- Rules management system
- Global and workspace-specific rules
- `/rules` command for rule management
- Session export functionality

### Changed
- Improved session management
- Enhanced memory system
- Better context handling

## [1.1.5] - 2025-11-01

### Added
- WebSocket server for real-time communication
- Live streaming AI responses
- Tool execution during streaming
- Auto-continuation feature

### Changed
- Improved chat interface
- Enhanced tool execution
- Better error messages

## [1.1.0] - 2025-10-20

### Added
- Initial public release
- Multi-provider AI support (OpenAI, Anthropic, Google, etc.)
- Agentic tools (file operations, command execution, web search)
- Interactive CLI with rich terminal interface
- Configuration management
- Session management
- Command auto-completion

### Changed
- Complete rewrite of core architecture
- Improved performance and stability
- Enhanced user experience

## [1.0.0] - 2025-10-16

### Added
- Initial beta release
- Basic chat functionality
- Provider integration
- File operations

---

## Version History

- **1.1.10** - MCP Support (Current)
- **1.1.10** - Voice Input & Vim Integration
- **1.1.8** - Multi-Model Testing & Web Search
- **1.1.7** - Local Model Support
- **1.1.6** - Rules Management
- **1.1.5** - WebSocket Server
- **1.1.0** - Initial Public Release
- **1.0.0** - Initial Beta Release

---

## Links

- [GitHub Repository](https://github.com/cognautic/cli)
- [Documentation](https://cognautic.vercel.app/cognautic-cli.html)
- [PyPI Package](https://pypi.org/project/cognautic-cli/)
- [MCP Documentation](https://modelcontextprotocol.io)

---

## Contributing

We welcome contributions! Please see our contributing guidelines for more information.

## License

MIT License - See LICENSE file for details
