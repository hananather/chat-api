Version 2 — Next Iteration (Placeholder)

Scope
- Starts as a copy of v1. Extend here with new features (e.g., streaming, auth, state, observability).

Run
```bash
uv run fastapi run --app-dir versions/v2 app.main:app --reload
```

Quick test
```bash
curl -s -X POST localhost:8000/chat \
  -H 'Content-Type: application/json' \
  -d '{"message":"Hello!"}' | jq
```

Environment
- COHERE_API_KEY
- COHERE_DEFAULT_MODEL

