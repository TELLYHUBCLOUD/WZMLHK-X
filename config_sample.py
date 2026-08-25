# REQUIRED CONFIG
BOT_TOKEN = ""
OWNER_ID = 0
TELEGRAM_API = 0
TELEGRAM_HASH = ""
DATABASE_URL = ""
KUMA_URL = ""

# OPTIONAL CONFIG
DEFAULT_LANG = "en"
TG_PROXY = {}  # {"scheme": ”socks5”, "hostname": ””, "port": 1234, "username": ”user”, "password": ”pass”}
USER_SESSION_STRING = ""
CMD_SUFFIX = ""
AUTHORIZED_CHATS = ""
SUDO_USERS = ""
STATUS_LIMIT = 10
DEFAULT_UPLOAD = "rc"
STATUS_UPDATE_INTERVAL = 15
FILELION_API = ""
STREAMWISH_API = ""
ALLDEBRID_API_KEY = ""
EXCLUDED_EXTENSIONS = ""
BLACKLISTED_KEYWORDS = (
    "hdcam camrip hdtc hdts predvd hc-hd 2160phd 1080phd 720phd hd-cam cam-rip"
)
INC_TASK_NOTIFY = False
INC_TASK_RESUME = False
YT_DLP_OPTIONS = ""
USE_SERVICE_ACCOUNTS = False
NAME_SWAP = ""
FFMPEG_CMDS = {}
UPLOAD_PATHS = {}
WEB_ACCESS_PASSWORD = (
    ""  # Secret for deriving proxy passwords. Logs derived passwords at startup.
)

# Hyper Tg Downloader
HELPER_TOKENS = ""
STREAM_TOKENS = ""
USE_HYPER = True

# MegaAPI v4.30
MEGA_EMAIL = ""
MEGA_PASSWORD = ""
DISABLE_MEGA = False

# Disable Options
DISABLE_TORRENTS = False
DISABLE_LEECH = False
DISABLE_MIRROR = False
DISABLE_BULK = False
DISABLE_MULTI = False
DISABLE_SEED = False
DISABLE_FF_MODE = False
DISABLE_JD = False
DISABLE_NZB = False
DISABLE_SEEDR = False
DISABLE_RSS = False
DISABLE_SEARCH = False
DISABLE_STREAM = False
DISABLE_YTDLP = False

# Telegraph
AUTHOR_NAME = "WZML-X"
AUTHOR_URL = "https://t.me/WZML_X"

# Task Limits
DIRECT_LIMIT = 0
MEGA_LIMIT = 0
TORRENT_LIMIT = 0
GD_DL_LIMIT = 0
RC_DL_LIMIT = 0
CLONE_LIMIT = 0
JD_LIMIT = 0
NZB_LIMIT = 0
SEEDR_LIMIT = 0
YTDLP_LIMIT = 0
PLAYLIST_LIMIT = 0
LEECH_LIMIT = 0
EXTRACT_LIMIT = 0
ARCHIVE_LIMIT = 0
STORAGE_LIMIT = 0
MONTHLY_BANDWIDTH = 0

# Percentage of currently free storage available to staged torrent batches (1-100).
STAGED_TORRENT_STORAGE_PERCENT = 50

# CPU limit for background services (SABnzbd, JDownloader). Default: 20
CPU_LIMIT = 20

# Throttle services during heavy ops (FFmpeg). auto=low-end only, always, never
THROTTLE_SERVICES = "auto"

# Image Search
USE_IMAGES = False
IMG_SEARCH = ""
IMG_PAGE = 1
IMG_SOURCES = ["wallpaperflare"]

# Insta video downloader api
INSTADL_API = ""

# Nzb search
HYDRA_IP = ""
HYDRA_API_KEY = ""

# Media Search
# Optional: Set IMDB_TEMPLATE to use old HTML format instead of Rich Messages.
# If empty (default), IMDb uses Rich Messages with tables and collapsible sections.
IMDB_TEMPLATE = ""

# Task Tools
FORCE_SUB_IDS = ""
MEDIA_STORE = True
DELETE_LINKS = False

# Limiters
BOT_MAX_TASKS = 0
USER_MAX_TASKS = 0
USER_TIME_INTERVAL = 0
VERIFY_TIMEOUT = 0
LOGIN_PASS = ""

# Crash Reporting
ENABLE_TELEMETRY = True  # Send crash reports to remote worker

# Bot Settings
BOT_PM = False
COLORED_BTNS = True
SET_COMMANDS = True
TIMEZONE = "Asia/Kolkata"

# GDrive Tools
GDRIVE_ID = ""
GD_DESP = "Uploaded with WZ Bot"
IS_TEAM_DRIVE = False
STOP_DUPLICATE = False
INDEX_URL = ""

# YT Tools
YT_DESP = "Uploaded to YouTube by WZML-X bot"
YT_TAGS = ["telegram", "bot", "youtube"]  # or as a comma-separated string
YT_CATEGORY_ID = 22
YT_PRIVACY_STATUS = "unlisted"

# Rclone
RCLONE_PATH = ""
RCLONE_FLAGS = ""
RCLONE_SERVE_URL = ""
RCLONE_USE_REMOTE_PREFIX = True
SHOW_CLOUD_LINK = True
RCLONE_SERVE_PORT = 0
RCLONE_SERVE_USER = ""
RCLONE_SERVE_PASS = ""

# For rclone list module
RCLONE_REMOTE = ""
REMOTE_BASE_PATH = ""

# JDownloader
JD_EMAIL = ""
JD_PASS = ""

# Seedr (magnet mirroring via seedr.cc)
SEEDR_EMAIL = ""
SEEDR_PASSWORD = ""
# Delete the folder from Seedr after the files are downloaded locally. Default: False
SEEDR_DELETE_FOLDER = False

# Sabnzbd
USENET_SERVERS = [
    {
        "name": "main",
        "host": "",
        "port": 563,
        "timeout": 60,
        "username": "",
        "password": "",
        "connections": 8,
        "ssl": 1,
        "ssl_verify": 2,
        "ssl_ciphers": "",
        "enable": 1,
        "required": 0,
        "optional": 0,
        "retention": 0,
        "send_group": 0,
        "priority": 0,
    }
]

# Update
UPSTREAM_REPO = ""
UPSTREAM_BRANCH = "master"
# Leech
LEECH_SPLIT_SIZE = 0
AS_DOCUMENT = False
EQUAL_SPLITS = False
MEDIA_GROUP = False
TRANSMISSION_MODE = "both"
LEECH_PREFIX = ""
LEECH_SUFFIX = ""
LEECH_FONT = ""
LEECH_CAPTION = ""
THUMBNAIL_LAYOUT = ""

# Log Channels
LEECH_DUMP_CHAT = ""
LINKS_LOG_ID = ""
MIRROR_LOG_ID = ""

# qBittorrent/Aria2c
TORRENT_TIMEOUT = 0
BASE_URL = ""
WEB_PINCODE = True

# Queueing system
QUEUE_ALL = 0
QUEUE_DOWNLOAD = 0
QUEUE_UPLOAD = 0

# RSS
RSS_DELAY = 600
RSS_CHAT = ""
RSS_SIZE_LIMIT = 0

# Torrent Search
SEARCH_API_LINK = ""
SEARCH_LIMIT = 0
SEARCH_PLUGINS = [
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/piratebay.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/limetorrents.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/torlock.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/torrentscsv.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/eztv.py",
    "https://raw.githubusercontent.com/qbittorrent/search-plugins/master/nova3/engines/torrentproject.py",
    "https://raw.githubusercontent.com/MaurizioRicci/qBittorrent_search_engines/master/kickass_torrent.py",
    "https://raw.githubusercontent.com/MaurizioRicci/qBittorrent_search_engines/master/yts_am.py",
    "https://raw.githubusercontent.com/MadeOfMagicAndWires/qBit-plugins/master/engines/linuxtracker.py",
    "https://raw.githubusercontent.com/MadeOfMagicAndWires/qBit-plugins/master/engines/nyaasi.py",
    "https://raw.githubusercontent.com/LightDestory/qBittorrent-Search-Plugins/master/src/engines/ettv.py",
    "https://raw.githubusercontent.com/LightDestory/qBittorrent-Search-Plugins/master/src/engines/glotorrents.py",
    "https://raw.githubusercontent.com/LightDestory/qBittorrent-Search-Plugins/master/src/engines/thepiratebay.py",
    "https://raw.githubusercontent.com/v1k45/1337x-qBittorrent-search-plugin/master/leetx.py",
    "https://raw.githubusercontent.com/nindogo/qbtSearchScripts/master/magnetdl.py",
    "https://raw.githubusercontent.com/msagca/qbittorrent_plugins/main/uniondht.py",
    "https://raw.githubusercontent.com/khensolomon/leyts/master/yts.py",
]


# ---- StarfallX v1.2 features (Video Tools / Poster / Auto-Process / Sites) ----
ARIA2_MAX_CONCURRENT_DOWNLOADS = 4
ARIA2_MAX_CONNECTION_PER_SERVER = 16
ARIA2_MAX_OVERALL_DOWNLOAD_LIMIT = "0"
ARIA2_MAX_OVERALL_UPLOAD_LIMIT = "1M"
ARIA2_MIN_SPLIT_SIZE = "1M"
ARIA2_SPLIT = 16
AUTORENAME = True
AUTORENAME_CLEAN_SEPARATORS = False
AUTO_AUDIO_ORDER = ""
AUTO_INTRO_SUBTITLE = False
AUTO_KEEP_AUDIO_LANGS = ""
AUTO_KEEP_SUBTITLE_LANGS = ""
AUTO_LEECH = False
AUTO_MERGE = False
AUTO_MERGE_SAFETY_MB = 150
AUTO_METADATA = True
AUTO_ORDER = False
AUTO_POSTER_ENABLED = False
AUTO_POSTER_USE_AS_THUMBNAIL = True
AUTO_PROCESS = False
AUTO_PROCESS_LOGS = False
AUTO_PROCESS_MESSAGE_MODE = "quiet"
AUTO_REMOVE_STREAMS = False
AUTO_RENAME = True
AUTO_SUBTITLE_ORDER = ""
AUTO_THUMBNAIL = False
AUTO_THUMBNAIL_QUALITY = 95
AUTO_UNZIP = False
AUTO_VT = False
BASE_URL_PORT = 80
BOT_THEME = "starfall"
CLEAN_LOG_MSG = False
FFMPEG_CPU_CORES = ""
FFMPEG_QUEUE_ENABLED = True
FFMPEG_QUEUE_LOGS = True
FFMPEG_THREADS = 0
INCOMPLETE_TASK_NOTIFIER = False
INTRO_SUBTITLE_COLOR = "&H00FFFFFF"
INTRO_SUBTITLE_COLOR_PALETTE = ""
INTRO_SUBTITLE_DURATION = 5
INTRO_SUBTITLE_FADE_MS = 400
INTRO_SUBTITLE_FONT = "Arial"
INTRO_SUBTITLE_FONT_SIZE = 54
INTRO_SUBTITLE_OUTLINE_COLOR = "&H00FF9E2D"
INTRO_SUBTITLE_RANGES = "00:00:00 - 00:00:05 (5s) | 00:01:20 - 00:01:25 (5s) | 00:02:40 - 00:02:45 (5s) | 00:04:00 - 00:04:05 (5s) | 00:05:20 - 00:05:25 (5s) | 00:06:40 - 00:06:45 (5s) | 00:08:00 - 00:08:05 (5s) | 00:09:20 - 00:09:25 (5s) | 00:10:40 - 00:10:45 (5s) | 00:12:00 - 00:12:05 (5s) | 00:13:20 - 00:13:25 (5s) | 00:14:40 - 00:14:45 (5s) | 00:16:00 - 00:16:05 (5s) | 00:17:20 - 00:17:25 (5s) | 00:18:40 - 00:18:45 (5s)"
INTRO_SUBTITLE_TEXT = ""
LEECH_COMPLETE_MSG = True
LEECH_FILENAME_REMNAME_AUTO = "[S{season}E{episode}] {title}   {resolution} {bit} {ott} {quality} {lib} [Tamil] ESub"
LEECH_FILENAME_REMNAME_REGEX = r"www\.1TamilMV\.[^\s]+"
LIBRE_TRANSLATE_API_KEY = ""
LIBRE_TRANSLATE_API_URL = ""
MAX_PARALLEL_TASKS = 0
MX_DEFAULT_AUDIO = "ask"
MX_PLAYER_API_BASE = "internal"
MYANIMELIST_CLIENT_ID = ""
MYANIMELIST_CLIENT_NAME = ""
PERFORMANCE_PROFILE = "auto"
POST_ANIME_CAPTION = (
        "<b>{title}</b>\n\n"
        "Quality: <code>{quality} {resolution} {bit} {codec}</code>\n"
        "Audio: <code>{audio}</code>\n"
        "Subtitles: <code>{subtitles}</code>\n\n"
        "<blockquote expandable>{synopsis}</blockquote>"
    )
POST_BRAND_NAME = "Anime Starfall"
POST_LOGO = ""
POST_MOVIE_CAPTION = (
        "<b>「 {title} - {year} 」</b>\n"
        "━━━━━━━━━━━━━━━━━━\n"
        "╔════◇═══════════◇════\n"
        "║ Season ➤ {season} ( {episodes} Episodes )\n"
        "║ IMBD ➤ {rating} Rating \n"
        "║ Genres ➤ {genres} \n"
        "║ Quality ➤ {resolution} {bit} {codec}\n"
        "║ Audio ➤ {languages} {audio_codec} {audio_channels} ~ {shortsub} \n"
        "╚════◇═══════════◇════\n\n"
        "<blockquote expandable>Synopsis :\n"
        "   {plot}</blockquote>"
    )
POST_TEMPLATE_ID = 1
POST_TV_CAPTION = (
        "<b>{title}</b> S{season}E{episode}\n\n"
        "Quality: <code>{quality} {resolution} {bit} {codec}</code>\n"
        "Audio: <code>{audio}</code>\n"
        "Subtitles: <code>{subtitles}</code>\n\n"
        "<blockquote expandable>{plot}</blockquote>"
    )
PREMIUM_UPLOAD_WORKERS = 2
QBIT_UPLOAD_LIMIT = 1048576
QUEUE_BYPASS_SIZE_GB = 1
RENAME_METHOD = "auto"
RSS_PARALLEL_DOWNLOADS = 8
RSS_PARALLEL_UPLOADS = 2
SAFE_CPU_PERCENT = 88
SAFE_FREE_RAM_MB = 768
SEQUENTIAL_LEECH = True
SITES_LINKS = ""
SITE_QUALITY_SELECTOR_TIMEOUT = 120
STATUS_THEME = "starfall"
SUBTITLE_TRANSLATE_PROVIDER = "libre"
SUBTITLE_TRANSLATE_TARGET = "en"
TG_COPY_DELAY = 0.15
TG_FLOOD_WAIT_MULTIPLIER = 1.1
THUMBNAIL_MODE = "automatic"
TMDB_ACCESS_TOKEN = ""
TMV_CATEGORY = "tamil"
TMV_SEEN_ITEMS = ""
UPDATE_PKGS = True
VIDEO_TOOLS_LOGS = True
VIDEO_TOOLS_REPLY_TIMEOUT = 30