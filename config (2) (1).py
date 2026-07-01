import os

# ── Telegram API Credentials ──────────────────────────────────────────────────
API_ID = int(os.getenv("API_ID", "38563100"))
API_HASH = os.getenv("API_HASH", "e17dad613bba83ff2a873d61faf2394f")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8727666158:AAEKbp5C3kWPA68BQhR_cjAYersOB1bfABg")

# ── Pyrogram String Session (for Voice Chat user) ─────────────────────────────
SESSION_STRING = os.getenv(
    "SESSION_STRING",
    "BQJMbRwAOe4pwMg8KBRIBojVY7QSglcyKr1mUfk_2fu7cY6JLGx9CAxBhZUpBOpq-zh2lKg6hKZhtEOcuBr8Pv9tGVFvdoZglFM9oa5GERDbH67D1Nrgc__msKBzTptI3kWDRPg5kJFquo5dyfjbsUspNqPTzSXfFDlAF6fbt-pemHELmuvW-C1V2I01OL3H5KQridcr8uP57iODxGg5y0U4F5ko5YmZTxrhv9DCXzFiSvuPzz5tYvTIQmQv1-DMpZNIWkximhVJg67Snl07pf-k-CdgrbRgDvrnA5Fl3SLrKbW5uiVO-bnEkbxfrmgbSjPGwkH18oBlQB-e43n8Nc40bAH6vQAAAAIO9FuDAA",
)

# ── Owner & Support ───────────────────────────────────────────────────────────
OWNER_ID = int(os.getenv("OWNER_ID", "8000127916"))

# ── Support Group (gets join/new user notifications) ─────────────────────────
# Set this to your support group chat_id (negative number for groups)
SUPPORT_GROUP_ID = int(os.getenv("SUPPORT_GROUP_ID", "0"))

# ── Limits ────────────────────────────────────────────────────────────────────
MAX_DURATION_SECONDS = 3600  # 1 hour max song duration
MAX_QUEUE_SIZE = 50  # Max songs in queue per chat
IDLE_TIMEOUT_SECONDS = 300  # Auto-leave if VC empty for 5 minutes
