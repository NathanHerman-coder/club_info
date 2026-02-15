# Mini e‑commerce (Flask)

Minimal e‑commerce scaffold using Flask, SQLite and SQLAlchemy.

Quick start

1. Create and activate a virtualenv (recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Initialize the database (once)

```bash
flask db init
flask db migrate -m "initial"
flask db upgrade
```

4. Run the app

```bash
python3 main.py
```

Notes

- This is a minimal example: orders are not persisted (checkout is simulated).
- Admin pages are unprotected; add authentication for production use.
