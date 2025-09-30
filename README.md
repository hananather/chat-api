# chat-api

Minimal FastAPI chat backend that powers a Cohere-based chat gateway.

## Blog Series

| Version | Focus | Link |
| --- | --- | --- |
| V1 | Building a simple chat gateway with FastAPI and Cohere | [docs/blog/chat-api/v1-simple-chat-gateway.md](docs/blog/chat-api/v1-simple-chat-gateway.md) |
| V2 | Coming soon | _Planned_ |
| V3 | Coming soon | _Planned_ |

More details and links: [docs/blog/chat-api/index.md](docs/blog/chat-api/index.md)

## Versioned App Structure

Each iteration lives in its own folder so you can run, compare, and revisit older versions easily:

```
versions/
  v1/
    app/
    experiments/
    README.md
  v2/
    app/
    experiments/
    README.md
```

Shared, cross-version code can live in a future `shared/` folder if needed.

## Run Locally

1) Install dependencies
```bash
uv sync
```

2) Set environment
```bash
cp .env.example .env  # and fill in COHERE_API_KEY, COHERE_DEFAULT_MODEL
```

3) Run V1
```bash
uv run fastapi run --app-dir versions/v1 app.main:app --reload
```

4) (Optional) Run V2
```bash
uv run fastapi run --app-dir versions/v2 app.main:app --reload
```

5) Quick test
```bash
curl -s -X POST localhost:8000/chat \
  -H 'Content-Type: application/json' \
  -d '{"message":"Hello!"}' | jq
```

- API docs: http://localhost:8000/docs
- OpenAPI JSON: http://localhost:8000/openapi.json
