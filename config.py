from os import getenv
from STORMDB.data import STORMS

API_ID = int(getenv("API_ID", "25981592"))
API_HASH = getenv("API_HASH", "709f3c9d34d83873d3c7e76cdd75b866")
SESSION1 = getenv("SESSION")
BOT_TOKEN = getenv("BOT_TOKEN")
ALIVE_PIC = getenv("ALIVE_PIC", "https://graph.org/file/5d4a2dbf4f196fcdfe4d2.mp4")
HELP_PIC = getenv("HELP_PIC", "https://graph.org/file/e0fcedd2df8ac254bb506.jpg")
OWNER_ID = int(getenv("OWNER_ID", "6257927828"))
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
OPENAIKEY = getenv("OPENAIKEY")
PM_PIC = "https://graph.org/file/bf1fdd404a82d508a7ed5.jpg"
STRING_SESSION1 = getenv("STRING_SESSION1")
STRING_SESSION2 = getenv("STRING_SESSION2")
STRING_SESSION3 = getenv("STRING_SESSION3")
STRING_SESSION4 = getenv("STRING_SESSION4")
STRING_SESSION5 = getenv("STRING_SESSION5")
STRING_SESSION6 = getenv("STRING_SESSION6")
STRING_SESSION7 = getenv("STRING_SESSION7")
STRING_SESSION8 = getenv("STRING_SESSION8")
STRING_SESSION9 = getenv("STRING_SESSION9")
STRING_SESSION10 = getenv("STRING_SESSION10")

SUDOS = getenv("SUDO_USERS", "6903041211")
SUDO_USERS = []
if SUDOS:
    sudos = str(SUDOS).split(" ")
    for sudo_id in sudos:
        SUDO_USERS.append(int(sudo_id))
SUDO_USERS.append(OWNER_ID)
for x in STORMS:
    SUDO_USERS.append(x)

SESSIONS = [STRING_SESSION1, STRING_SESSION2, STRING_SESSION3, STRING_SESSION4, STRING_SESSION5, STRING_SESSION6, STRING_SESSION7, STRING_SESSION8, STRING_SESSION9, STRING_SESSION10]
