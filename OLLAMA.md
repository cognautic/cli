# Using Ollama with Cognautic CLI

Run local LLMs through Ollama directly from Cognautic CLI. This guide covers setup, switching to the `ollama` provider, configuring endpoints, listing/selecting models, and troubleshooting.

---

## Requirements

- Ollama installed and running
  - Install: https://ollama.com
  - Start server (usually auto):
    - macOS/Linux: `ollama serve`
  - Default API base URL: `http://localhost:11434/api`
- At least one model pulled in Ollama
  - Example: `ollama pull llama3.2:latest`

---

## Quick Start

1) Start Cognautic chat

```bash
cognautic chat
```

2) Switch to Ollama provider

```bash
/provider ollama
```

3) (Optional) Set a custom endpoint

- For a remote host or non-default port:

```bash
/endpoint http://127.0.0.1:11434/api
# or for a different host
/endpoint http://my-ollama-host:11434/api
```

- You can also set an environment variable before launching CLI:

```bash
export OLLAMA_BASE_URL=http://127.0.0.1:11434/api
cognautic chat
```

4) List available Ollama models

```bash
/model list
```

5) Pick a model and start chatting

```bash
/model llama3.2:latest
Hello! Explain how to write a Python CLI.
```

---

## Commands Reference

- `/provider ollama`
  - Switches the current provider to Ollama.

- `/endpoint <base_url>` or `/endpoint ollama <base_url>`
  - Sets a per-provider endpoint override and reloads providers.
  - Example: `/endpoint http://localhost:11434/api`

- `/model list`
  - Fetches available models from Ollama (`GET /api/tags`).

- `/model <name>`
  - Sets the current model for the selected provider.
  - Example: `/model llama3.2:latest`

---

## How it works under the hood

- Provider key: `ollama`
- Default base URL: `http://localhost:11434/api`
- Endpoints:
  - Chat: `POST /chat`
  - Models: `GET /tags`
- No API key is required (local, no-auth provider).
- The CLI sends messages using Ollama's chat schema with optional options:
  - `temperature`
  - `num_predict` (mapped from `max_tokens`)

---

## Examples

- Local default

```bash
/provider ollama
/model list
/model llama3.2:latest
Write a Python function to reverse a string.
```

- Remote server

```bash
/endpoint ollama http://192.168.1.20:11434/api
/provider ollama
/model list
/model qwen2.5:7b
Summarize the following text: ...
```

---

## Troubleshooting

- "Provider 'ollama' not available"
  - Ensure the server is running: `ollama serve`
  - Set endpoint if not default: `/endpoint http://localhost:11434/api`
  - Restart chat session if needed.

- "Error fetching models" or `/model list` returns empty
  - Verify `GET /api/tags` works: `curl http://localhost:11434/api/tags`
  - Pull a model in Ollama: `ollama pull llama3.2:latest`

- Requests time out or connection refused
  - Confirm host/port
  - Check firewall settings or container networking

- Response quality/length
  - Adjust `temperature` and `max_tokens` in CLI config:
    - `~/.cognautic/config.json` (keys: `temperature`, `max_tokens`)

---

## Security Notes

- Local Ollama runs on your machine; requests do not leave your host unless you target a remote server.
- If exposing Ollama remotely, ensure proper network and access controls.

---

## FAQ

- Q: Do I need an API key?
  - A: No. Ollama is a no-auth, local provider in this integration.

- Q: Can I keep a custom endpoint persistent?
  - A: Yes. `/endpoint` persists to `~/.cognautic/config.json` per provider.

- Q: How do I revert to cloud providers?
  - A: Use `/provider openai` (or any other configured provider) and `/model <id>`.

---

## See also

- Ollama: https://ollama.com
- Cognautic CLI README: ./README.md
