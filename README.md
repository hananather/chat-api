# chat-api

Minimal FastAPI chat backend that powers a Cohere-based chat gateway.

## Blog Series

| Version | Focus | Link |
| --- | --- | --- |
| V1 | Building a simple chat gateway with FastAPI and Cohere | [docs/blog/chat-api/v1-simple-chat-gateway.md](docs/blog/chat-api/v1-simple-chat-gateway.md) |
| V2 | Coming soon | _Planned_ |
| V3 | Coming soon | _Planned_ |

## Getting Started

```bash
uv sync
uv run fastapi run app.main:app --reload
```

Set your Cohere credentials in `.env` before starting the server.
