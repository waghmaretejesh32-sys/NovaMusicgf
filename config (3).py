import os

# Your Telegram API Credentials
API_ID = int(os.getenv("API_ID", "38563100"))  # Replace with your API ID
API_HASH = os.getenv("API_HASH", "e17dad613bba83ff2a873d61faf2394f")  # Replace with your API Hash
BOT_TOKEN = os.getenv("BOT_TOKEN", "8727666158:AAEKbp5C3kWPA68BQhR_cjAYersOB1bfABg")  # Replace with your Bot Token

# A Pyrogram String Session for the User account that will join the Voice Chat
SESSION_STRING = os.getenv("SESSION_STRING", "BQJMbRwAOe4pwMg8KBRIBojVY7QSglcyKr1mUfk_2fu7cY6JLGx9CAxBhZUpBOpq-zh2lKg6hKZhtEOcuBr8Pv9tGVFvdoZglFM9oa5GERDbH67D1Nrgc__msKBzTptI3kWDRPg5kJFquo5dyfjbsUspNqPTzSXfFDlAF6fbt-pemHELmuvW-C1V2I01OL3H5KQridcr8uP57iODxGg5y0U4F5ko5YmZTxrhv9DCXzFiSvuPzz5tYvTIQmQv1-DMpZNIWkximhVJg67Snl07pf-k-CdgrbRgDvrnA5Fl3SLrKbW5uiVO-bnEkbxfrmgbSjPGwkH18oBlQB-e43n8Nc40bAH6vQAAAAIO9FuDAA")
# Command prefix
PREFIX = "/"

# Bot Owner ID
OWNER_ID = int(os.getenv("OWNER_ID", "8000127916"))

# YT-DLP Cookie Configuration
YTDL_COOKIEFILE = os.getenv("YTDL_COOKIEFILE", None)
YTDL_COOKIES_CONTENT = os.getenv("YTDL_COOKIES_CONTENT", None)
