# MCP Support - Quick Reference

## What is MCP?

**Model Context Protocol (MCP)** is an open standard that allows AI systems to connect with external data sources and tools. Think of it as a universal adapter that lets Cognautic CLI talk to other services.

## Quick Start

### 1. View Available Servers
```bash
/mcp config
```

### 2. Connect to a Server
```bash
/mcp connect filesystem
```

### 3. List Available Tools
```bash
/mcp tools
```

### 4. Use MCP Tools
Just ask the AI naturally:
```
You: List all Python files in my project using the filesystem MCP server
```

## Common Commands

| Command | Description |
|---------|-------------|
| `/mcp` | Show MCP help |
| `/mcp list` | List connected servers |
| `/mcp connect <server>` | Connect to a server |
| `/mcp disconnect <server>` | Disconnect from a server |
| `/mcp tools` | List available tools |
| `/mcp resources` | List available resources |
| `/mcp config` | Show configuration |

## Pre-configured Servers

### Filesystem Server
Access local files and directories
```bash
/mcp connect filesystem
```

### GitHub Server
Interact with GitHub repositories (requires token)
```bash
# Set your token in ~/.cognautic/mcp_servers.json first
/mcp connect github
```

### PostgreSQL Server
Query PostgreSQL databases (requires connection string)
```bash
# Set connection string in ~/.cognautic/mcp_servers.json first
/mcp connect postgres
```

## Configuration File

Edit `~/.cognautic/mcp_servers.json` to add or modify servers:

```json
{
  "servers": {
    "my-server": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-name"],
      "env": {
        "API_KEY": "your_key_here"
      },
      "transport": "stdio"
    }
  }
}
```

## Example Workflow

```bash
# Start Cognautic
cognautic chat

# Connect to filesystem server
/mcp connect filesystem

# Ask AI to use it
You: Show me all JavaScript files in the src directory

# The AI will use the MCP filesystem server to list files
AI: I'll use the filesystem MCP server to list JavaScript files...
```

## Troubleshooting

### Server won't connect
- Check that `npx` is installed: `npm install -g npx`
- Verify the server package exists
- Check environment variables are set

### Tools not showing
- Ensure server is connected: `/mcp list`
- Try disconnecting and reconnecting
- Check server logs

### Permission errors
- Verify file/directory permissions
- Check environment variable values
- Ensure API tokens are valid

## More Information

For detailed documentation, see [MCP_SUPPORT.md](MCP_SUPPORT.md)

For the official MCP specification, visit [modelcontextprotocol.io](https://modelcontextprotocol.io)
