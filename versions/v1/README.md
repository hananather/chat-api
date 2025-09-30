Version 1 — Simple Chat Gateway

Scope
- Single POST /chat endpoint
- Cohere Chat API integration
- Minimal timing and request_id in response

Run
```bash
uv run fastapi run --app-dir versions/v1 app.main:app --reload
```

Quick test
```bash
curl -s -X POST localhost:8000/chat \
  -H 'Content-Type: application/json' \
  -d '{"message":"Hello!"}' | jq
```

Environment
- COHERE_API_KEY
- COHERE_DEFAULT_MODEL (e.g., command-r-plus-08-2024)

