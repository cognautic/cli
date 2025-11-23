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

---
