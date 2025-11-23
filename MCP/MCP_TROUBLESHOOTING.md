# MCP Troubleshooting Guide

## Issue: Connected but 0 Tools/Resources/Prompts

If you see this when connecting to an MCP server:

```
INFO: Connected to filesystem
  Tools: 0
  Resources: 0
  Prompts: 0
```

This means the connection succeeded but capability discovery failed. Here are the common causes and solutions:

### 1. MCP Server Not Installed

**Problem:** The MCP server package isn't installed.

**Solution:**
```bash
# Install the filesystem MCP server
npm install -g @modelcontextprotocol/server-filesystem

# Verify installation
npx @modelcontextprotocol/server-filesystem --help
```

### 2. npx Not Found

**Problem:** `npx` command is not available.

**Solution:**
```bash
# Install Node.js and npm (includes npx)
# On Ubuntu/Debian:
sudo apt update
sudo apt install nodejs npm

# On macOS:
brew install node

# On Arch Linux:
sudo pacman -S nodejs npm

# Verify installation
npx --version
```

### 3. Server Not Responding

**Problem:** The MCP server starts but doesn't respond to capability requests.

**Solution:**
```bash
# Test the server manually
npx -y @modelcontextprotocol/server-filesystem /tmp

# If it hangs or errors, the server may not be compatible
# Try a different version or server
```

### 4. Incorrect Configuration

**Problem:** Server configuration in `~/.cognautic/mcp_servers.json` is incorrect.

**Solution:**
Check your configuration file:
```bash
cat ~/.cognautic/mcp_servers.json
```

Should look like:
```json
{
  "servers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/home/user"],
      "env": {},
      "transport": "stdio"
    }
  }
}
```

**Fix:** Update the path in args to a valid directory on your system.

### 5. Enable Debug Logging

To see detailed error messages:

```bash
# Set logging level before starting Cognautic
export COGNAUTIC_LOG_LEVEL=DEBUG
cognautic chat
```

Then check the logs for MCP-related errors.

### 6. Test with a Simple MCP Server

Create a minimal test server to verify MCP is working:

**test_mcp_server.py:**
```python
#!/usr/bin/env python3
import json
import sys

def send_message(msg):
    sys.stdout.write(json.dumps(msg) + "\n")
    sys.stdout.flush()

def read_message():
    line = sys.stdin.readline()
    return json.loads(line) if line else None

# Main loop
while True:
    msg = read_message()
    if not msg:
        break
    
    if msg.get("method") == "initialize":
        send_message({
            "jsonrpc": "2.0",
            "id": msg["id"],
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {
                    "tools": {},
                    "resources": {}
                },
                "serverInfo": {
                    "name": "test-server",
                    "version": "1.0.0"
                }
            }
        })
    elif msg.get("method") == "tools/list":
        send_message({
            "jsonrpc": "2.0",
            "id": msg["id"],
            "result": {
                "tools": [
                    {
                        "name": "test_tool",
                        "description": "A test tool",
                        "inputSchema": {
                            "type": "object",
                            "properties": {}
                        }
                    }
                ]
            }
        })
    elif msg.get("method") == "resources/list":
        send_message({
            "jsonrpc": "2.0",
            "id": msg["id"],
            "result": {
                "resources": []
            }
        })
    elif msg.get("method") == "prompts/list":
        send_message({
            "jsonrpc": "2.0",
            "id": msg["id"],
            "result": {
                "prompts": []
            }
        })
```

Add to `~/.cognautic/mcp_servers.json`:
```json
{
  "servers": {
    "test": {
      "command": "python3",
      "args": ["/path/to/test_mcp_server.py"],
      "env": {},
      "transport": "stdio"
    }
  }
}
```

Then test:
```bash
cognautic chat
/mcp connect test
```

If this works (shows 1 tool), the issue is with the specific MCP server, not Cognautic.

### 7. Check Server Stderr

The MCP server may be writing errors to stderr. Check if there are any error messages when connecting.

### 8. Verify Server Compatibility

Ensure the MCP server supports the protocol version `2024-11-05`. Some older servers may not be compatible.

### Quick Fix: Use Official MCP Servers

The most reliable MCP servers are the official ones from Anthropic:

```bash
# Install official servers
npm install -g @modelcontextprotocol/server-filesystem
npm install -g @modelcontextprotocol/server-github
npm install -g @modelcontextprotocol/server-memory

# Test filesystem server
npx @modelcontextprotocol/server-filesystem --help
```

## Still Having Issues?

1. Check the [MCP GitHub Issues](https://github.com/modelcontextprotocol/servers/issues)
2. Verify Node.js version: `node --version` (should be 18+)
3. Try reinstalling the MCP server: `npm uninstall -g @modelcontextprotocol/server-filesystem && npm install -g @modelcontextprotocol/server-filesystem`
4. Check Cognautic logs for detailed error messages
5. Open an issue on [Cognautic GitHub](https://github.com/cognautic/cli/issues) with:
   - Your OS and version
   - Node.js version
   - MCP server being used
   - Full error output

## Common Error Messages

### "command not found: npx"
Install Node.js and npm.

### "Empty response from MCP server"
The server isn't responding. Check if it's installed and the command is correct.

### "Timeout waiting for response"
The server is taking too long. Try increasing the timeout or check server performance.

### "Failed to initialize MCP server"
The server rejected the initialization. Check server logs and compatibility.
