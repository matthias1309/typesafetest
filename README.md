# typesafetest

Minimal demo of the [TypeSafe](https://typesafe.ai) AI SDK: judges a support
ticket with all three primitives (Noul, Choice, Score) in one request.

## Setup

```bash
python3 -m venv .venv && source .venv/bin/activate   # Python >= 3.10
pip install -r requirements.txt
export TYPESAFE_API_KEY=sk-...   # from https://console.typesafe.ai/keys
python demo.py
```
