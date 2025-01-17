from Esproritik.core.bot import Loy
from Esproritik.core.dir import dirr
from Esproritik.core.git import git
from Esproritik.core.userbot import Userbot
from Esproritik.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Loy()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
