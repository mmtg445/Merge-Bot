import os


class Config(object):
    API_HASH = os.environ.get("API_HASH", "8564fab8db759bb04b1907bd12ed98ef")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7860716079:AAFCAo1JQsbBqMhBjx5kJ93D6Ng6Mo1o0go")
    TELEGRAM_API = os.environ.get("TELEGRAM_API", "21188057")
    OWNER = os.environ.get("OWNER", "8102446291")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "RahatVx")
    PASSWORD = os.environ.get("PASSWORD", "rindex")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://rohanahamed75:gt4RXJZ1mUtOh4Xv@mmtg.0ong5.mongodb.net/?retryWrites=true&w=majority&appName=mmtg")
    LOGCHANNEL = os.environ.get("LOGCHANNEL" ,"-1002289024376")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
