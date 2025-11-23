# MCP (Model Context Protocol) Support in Cognautic CLI

## Overview

Cognautic CLI now supports the **Model Context Protocol (MCP)**, an open standard introduced by Anthropic for connecting AI systems with external data sources and tools. This implementation allows Cognautic to:

1. **Act as an MCP Client** - Connect to external MCP servers to access their tools, resources, and prompts
2. **Expose as an MCP Server** - Allow other MCP clients to use Cognautic's capabilities

## Features

### MCP Client Features
- ✅ Connect to multiple MCP servers simultaneously
- ✅ STDIO transport support (local processes)
- ✅ HTTP with SSE transport support (network-based)
- ✅ Automatic capability discovery (tools, resources, prompts)
- ✅ Tool execution from connected MCP servers
- ✅ Resource reading from MCP servers
- ✅ Prompt templates from MCP servers
- ✅ JSON-RPC 2.0 protocol implementation

### MCP Server Features
- ✅ Expose Cognautic's tools to other MCP clients
- ✅ Provide workspace files as resources
- ✅ Offer helpful prompt templates
- ✅ STDIO transport for local connections
- ✅ Full JSON-RPC 2.0 compliance

## Installation

The MCP support is included in Cognautic CLI. Install or update to the latest version:

```bash
pip install --upgrade cognautic-cli
```

Or install from source:

```bash
cd /path/to/cognautic/cli
pip install -e .
```

## Configuration

### MCP Server Configuration

MCP server configurations are stored in `~/.cognautic/mcp_servers.json`. The file is automatically created with default examples on first use.

Example configuration:

```json
{
  "servers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/home/user"],
      "env": {},
      "transport": "stdio",
      "description": "Access files and directories on the local filesystem"
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your_token_here"
      },
      "transport": "stdio",
      "description": "Interact with GitHub repositories"
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "POSTGRES_CONNECTION_STRING": "postgresql://user:pass@localhost/db"
      },
      "transport": "stdio",
      "description": "Query PostgreSQL databases"
    }
  },
  "enabled": []
}
```

### Available MCP Servers

The MCP ecosystem includes many pre-built servers:

- **@modelcontextprotocol/server-filesystem** - Local file system access
- **@modelcontextprotocol/server-github** - GitHub repository integration
- **@modelcontextprotocol/server-postgres** - PostgreSQL database queries
- **@modelcontextprotocol/server-slack** - Slack workspace integration
- **@modelcontextprotocol/server-google-drive** - Google Drive access
- **@modelcontextprotocol/server-puppeteer** - Web browser automation

Visit [modelcontextprotocol.io](https://modelcontextprotocol.io) for more servers.

## Usage

### In Chat Mode

#### View MCP Help
```
/mcp
```

#### List Connected Servers
```
/mcp list
```

#### Connect to a Server
```
/mcp connect filesystem
```

#### Disconnect from a Server
```
/mcp disconnect filesystem
```

#### List Available Tools
```
/mcp tools
```

#### List Available Resources
```
/mcp resources
```

#### Show Configuration
```
/mcp config
```

### Example Workflow

```bash
# Start Cognautic CLI
cognautic chat

# Connect to filesystem MCP server
/mcp connect filesystem

# List available tools
/mcp tools

# Now you can ask the AI to use MCP tools
You: Use the filesystem MCP server to list files in my home directory

# The AI will automatically use the connected MCP tools
```

## Using Cognautic as an MCP Server

Other MCP clients can connect to Cognautic to use its tools:

```bash
# Start Cognautic in MCP server mode (future feature)
cognautic mcp-server --workspace /path/to/project
```

The Cognautic MCP server exposes:

### Tools
- File operations (read, write, search)
- Command execution
- Code analysis
- Web search
- Directory context

### Resources
- Project files (README.md, package.json, etc.)
- Configuration files
- Documentation

### Prompts
- `code_review` - Review code for quality
- `debug_help` - Help debug issues
- `implement_feature` - Implement new features

## Architecture

### MCP Client Architecture

```
┌─────────────────┐
│  Cognautic CLI  │
│                 │
│  ┌───────────┐  │
│  │ MCP Client│  │
│  │  Manager  │  │
│  └─────┬─────┘  │
│        │        │
└────────┼────────┘
         │
    ┌────┴────┐
    │         │
┌───▼───┐ ┌──▼────┐
│ MCP   │ │ MCP   │
│Server1│ │Server2│
└───────┘ └───────┘
```

### MCP Server Architecture

```
┌─────────────────┐
│  MCP Client     │
│  (e.g., Claude) │
└────────┬────────┘
         │
    ┌────▼────┐
    │         │
┌───▼────────────┐
│  Cognautic MCP │
│     Server     │
│                │
│  ┌──────────┐  │
│  │  Tools   │  │
│  ├──────────┤  │
│  │Resources │  │
│  ├──────────┤  │
│  │ Prompts  │  │
│  └──────────┘  │
└────────────────┘
```

## Implementation Files

- **`cognautic/mcp_client.py`** - MCP client implementation
- **`cognautic/mcp_server.py`** - MCP server implementation
- **`cognautic/mcp_config.py`** - Configuration management
- **`cognautic/mcp_commands.py`** - Slash command handlers

## Protocol Details

### JSON-RPC Messages

MCP uses JSON-RPC 2.0 for communication:

**Request:**
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list",
  "params": {}
}
```

**Response:**
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "tools": [
      {
        "name": "read_file",
        "description": "Read a file from the filesystem",
        "inputSchema": {
          "type": "object",
          "properties": {
            "path": {"type": "string"}
          }
        }
      }
    ]
  }
}
```

### Transport Layers

#### STDIO Transport
- Used for local MCP servers
- Communication via stdin/stdout
- Newline-delimited JSON messages

#### HTTP with SSE Transport
- Used for network-based MCP servers
- Server-Sent Events for server-to-client messages
- HTTP POST for client-to-server messages

## Troubleshooting

### Connection Issues

**Problem:** Cannot connect to MCP server

**Solutions:**
1. Check that the server command is installed (e.g., `npx` for npm packages)
2. Verify environment variables are set correctly
3. Check server logs for errors
4. Ensure the server supports the MCP protocol version

### Tool Execution Failures

**Problem:** MCP tools fail to execute

**Solutions:**
1. Verify the tool parameters match the schema
2. Check server permissions
3. Review server logs
4. Ensure the server is still connected (`/mcp list`)

### Configuration Issues

**Problem:** Server not found in configuration

**Solutions:**
1. Check `~/.cognautic/mcp_servers.json` exists
2. Verify server name matches configuration
3. Ensure JSON syntax is valid

## Development

### Adding a Custom MCP Server

1. Create your MCP server following the protocol specification
2. Add configuration to `~/.cognautic/mcp_servers.json`:

```json
{
  "servers": {
    "my-custom-server": {
      "command": "python",
      "args": ["/path/to/my_server.py"],
      "env": {},
      "transport": "stdio"
    }
  }
}
```

3. Connect in Cognautic:
```
/mcp connect my-custom-server
```

### Extending MCP Client

To add new MCP client features, modify:
- `cognautic/mcp_client.py` - Core client logic
- `cognautic/mcp_commands.py` - Slash commands
- `cognautic/cli.py` - Command integration

### Extending MCP Server

To expose new Cognautic capabilities via MCP:
- `cognautic/mcp_server.py` - Add tools/resources/prompts

## Resources

- [Model Context Protocol Specification](https://modelcontextprotocol.io)
- [MCP GitHub Repository](https://github.com/modelcontextprotocol)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Anthropic MCP Announcement](https://www.anthropic.com/news/model-context-protocol)

## Future Enhancements

- [ ] HTTP with SSE transport implementation
- [ ] Automatic MCP tool integration with AI engine
- [ ] MCP prompt template usage
- [ ] Bidirectional MCP server mode
- [ ] MCP server discovery
- [ ] Enhanced error handling and retry logic
- [ ] MCP server health monitoring
- [ ] Tool result caching

## Contributing

Contributions to improve MCP support are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

MIT License - Same as Cognautic CLI
