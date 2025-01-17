from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", None)

<<<<<<< HEAD
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/EsproSupport")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/EsproUpdate")
=======
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/EsproSupport")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/EsproUpdate")
>>>>>>> 9589dde20b69bbd1f8e86e1d87e268b5b43c69ae

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "8007286147").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
