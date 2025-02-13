import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", "6109531260"))
API_ID = int(getenv("API_ID", "25374274")) #oP
API_HASH = getenv("API_HASH", "d0012f0876e6f9308eec2f474e7b9273")
