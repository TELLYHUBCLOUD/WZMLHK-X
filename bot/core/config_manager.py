from ast import literal_eval
from importlib import import_module
from os import getenv
from wz_bin import bin_name


class Config:
    ALLDEBRID_API_KEY = ""
    AS_DOCUMENT = False
    AUTHORIZED_CHATS = ""
    BASE_URL = ""
    BOT_TOKEN = ""
    HELPER_TOKENS = ""
    HELPER_STRINGS = ""
    STREAM_TOKENS = ""
    HELPER_BOT_PROXIES = ""
    HELPER_USER_PROXIES = ""
    BOT_MAX_TASKS = 0
    BOT_PM = False
    CMD_SUFFIX = ""
    COLORED_BTNS = True
    DEFAULT_LANG = "en"
    DATABASE_URL = ""
    DEFAULT_UPLOAD = "rc"
    DELETE_LINKS = False
    DEBRID_LINK_API = ""
    DISABLE_TORRENTS = False
    DISABLE_LEECH = False
    DISABLE_MIRROR = False
    DISABLE_BULK = False
    DISABLE_MULTI = False
    DISABLE_SEED = False
    DISABLE_FF_MODE = False
    DISABLE_MEGA = False
    DISABLE_JD = True
    DISABLE_NZB = True
    DISABLE_SEEDR = True
    DISABLE_RSS = False
    DISABLE_SEARCH = False
    DISABLE_STREAM = False
    DISABLE_YTDLP = False
    EQUAL_SPLITS = False
    EXCLUDED_EXTENSIONS = ""
    BLACKLISTED_KEYWORDS = ""
    FFMPEG_CMDS = {}
    FILELION_API = ""
    MEDIA_STORE = True
    FORCE_SUB_IDS = ""
    GOFILE_API = ""
    GOFILE_FOLDER_ID = ""
    GOFILE_AUTO_CREATE_FOLDER = False
    PIXELDRAIN_KEY = ""
    PROTECTED_API = ""
    BUZZHEAVIER_API = ""
    DEVUPLOADS_KEY = ""
    DEVUPLOADS_FOLDER = ""
    VIKINGFILE_HASH = ""
    VIKINGFILE_FOLDER = ""
    GDRIVE_ID = ""
    GD_DESP = "Uploaded with WZ Bot"
    AUTHOR_NAME = "WZML-X"
    AUTHOR_URL = "https://t.me/WZML_X"
    INSTADL_API = ""
    IMDB_TEMPLATE = ""
    IMAGES = []
    IMG_SEARCH = ""
    IMG_PAGE = 1
    USE_IMAGES = False
    IMG_SOURCES = ["wallpaperflare"]
    INC_TASK_NOTIFY = False
    INC_TASK_RESUME = False
    INDEX_URL = ""
    IS_TEAM_DRIVE = False
    JD_EMAIL = ""
    JD_PASS = ""
    SEEDR_EMAIL = ""
    SEEDR_PASSWORD = ""
    SEEDR_DELETE_FOLDER = False
    KUMA_URL = ""
    MEGA_EMAIL = ""
    MEGA_PASSWORD = ""
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
    STAGED_TORRENT_STORAGE_PERCENT = 50
    LEECH_DUMP_CHAT = ""
    LINKS_LOG_ID = ""
    MIRROR_LOG_ID = ""
    LEECH_PREFIX = ""
    LEECH_CAPTION = ""
    LEECH_SUFFIX = ""
    LEECH_FONT = ""
    LEECH_SPLIT_SIZE = 2097152000
    MEDIA_GROUP = False
    USE_HYPER = True
    HYPER_THREADS = 0
    HYPER_PIPELINE = 4
    HYPER_CHUNK = 512 * 1024
    STREAM_PIPELINE = 8
    STREAM_CHUNK = 1048576
    STREAM_PER_CLIENT = 6
    STREAM_GATE = 96
    CPU_LIMIT = 20
    THROTTLE_SERVICES = "auto"
    HYDRA_IP = ""
    HYDRA_API_KEY = ""
    NAME_SWAP = ""
    OWNER_ID = 0
    QUEUE_ALL = 0
    QUEUE_DOWNLOAD = 0
    QUEUE_UPLOAD = 0
    RCLONE_FLAGS = ""
    RCLONE_PATH = ""
    RCLONE_SERVE_URL = ""
    RCLONE_USE_REMOTE_PREFIX = True
    SHOW_CLOUD_LINK = True
    RCLONE_SERVE_USER = ""
    RCLONE_SERVE_PASS = ""
    RCLONE_SERVE_PORT = 8081
    RCLONE_REMOTE = ""
    REMOTE_BASE_PATH = ""
    RSS_CHAT = ""
    RSS_DELAY = 600
    RSS_SIZE_LIMIT = 0
    SEARCH_API_LINK = ""
    SEARCH_LIMIT = 0
    SEARCH_PLUGINS = []
    SET_COMMANDS = True
    STATUS_LIMIT = 10
    STATUS_UPDATE_INTERVAL = 15
    STOP_DUPLICATE = False
    STREAMWISH_API = ""
    SUDO_USERS = ""
    TELEGRAM_API = 0
    TELEGRAM_HASH = ""
    TG_PROXY = None
    THUMBNAIL_LAYOUT = ""
    VERIFY_TIMEOUT = 0
    LOGIN_PASS = ""
    TORRENT_TIMEOUT = 0
    TIMEZONE = "Asia/Kolkata"
    USER_MAX_TASKS = 0
    USER_TIME_INTERVAL = 0
    UPLOAD_PATHS = {}
    DRIVE_CATEGORY_MODE = False
    DRIVE_CATEGORY_SA = ""
    UPSTREAM_REPO = ""
    UPSTREAM_BRANCH = "master"
    USENET_SERVERS = []
    USER_SESSION_STRING = ""
    TRANSMISSION_MODE = "both"
    USE_SERVICE_ACCOUNTS = False
    ENABLE_TELEMETRY = True
    WEB_ACCESS_PASSWORD = ""
    WEB_PINCODE = True
    YT_DLP_OPTIONS = {}
    YT_DESP = "Uploaded with WZML-X bot"
    YT_TAGS = ["telegram", "bot", "youtube"]
    YT_CATEGORY_ID = 22
    YT_PRIVACY_STATUS = "unlisted"

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

    @classmethod
    def get(cls, key):
        return getattr(cls, key) if hasattr(cls, key) else None

    @classmethod
    def set(cls, key, value):
        if hasattr(cls, key):
            value = cls._convert_env_type(key, value)
            setattr(cls, key, value)
        else:
            raise KeyError(f"{key} is not a valid configuration key.")

    @classmethod
    def get_all(cls):
        return {
            key: getattr(cls, key)
            for key in cls.__dict__.keys()
            if not key.startswith("__") and not callable(getattr(cls, key))
        }

    @classmethod
    def load(cls):
        cls.load_config()
        cls.load_env()

    @classmethod
    def load_config(cls):
        try:
            settings = import_module("config")
        except ModuleNotFoundError:
            return
        for attr in dir(settings):
            if hasattr(cls, attr):
                value = getattr(settings, attr)
                if not value and not isinstance(value, (bool, int, float)):
                    continue
                if isinstance(value, str):
                    value = value.strip()
                if attr == "DEFAULT_UPLOAD" and value != "gd":
                    value = "rc"
                elif attr in [
                    "BASE_URL",
                    "RCLONE_SERVE_URL",
                    "INDEX_URL",
                    "SEARCH_API_LINK",
                    "KUMA_URL",
                ]:
                    if value:
                        value = value.strip("/")
                elif attr == "USENET_SERVERS":
                    try:
                        if not value[0].get("host"):
                            continue
                    except Exception:
                        continue
                setattr(cls, attr, value)
        for key in ["BOT_TOKEN", "OWNER_ID", "TELEGRAM_API", "TELEGRAM_HASH"]:
            value = getattr(cls, key)
            if isinstance(value, str):
                value = value.strip()
            if not value:
                raise ValueError(f"{key} variable is missing!")

    @classmethod
    def load_env(cls):
        config_vars = cls.get_all()
        for key in config_vars:
            env_value = getenv(key)
            if env_value is not None:
                converted_value = cls._convert_env_type(key, env_value)
                cls.set(key, converted_value)

    @classmethod
    def _convert_env_type(cls, key, value):
        original_value = getattr(cls, key, None)
        if original_value is None:
            return value
        elif isinstance(original_value, bool):
            if isinstance(value, bool):
                return value
            return str(value).lower() in ("true", "1", "yes")
        elif isinstance(original_value, int):
            if isinstance(value, int):
                return value
            try:
                return int(value)
            except (ValueError, TypeError):
                return original_value
        elif isinstance(original_value, float):
            if isinstance(value, float):
                return value
            try:
                return float(value)
            except (ValueError, TypeError):
                return original_value
        elif isinstance(original_value, list):
            if isinstance(value, list):
                return value
            if isinstance(value, str):
                try:
                    parsed = literal_eval(value)
                    if isinstance(parsed, list):
                        return parsed
                except (ValueError, SyntaxError):
                    pass
                if value.startswith("[") and value.endswith("]"):
                    return original_value
                return [v.strip() for v in value.split(",") if v.strip()]
            return original_value
        elif isinstance(original_value, dict):
            if isinstance(value, dict):
                return value
            if isinstance(value, str):
                try:
                    parsed = literal_eval(value)
                    if isinstance(parsed, dict):
                        return parsed
                except (ValueError, SyntaxError):
                    pass
            return original_value
        return value

    @classmethod
    def load_dict(cls, config_dict):
        for key, value in config_dict.items():
            if hasattr(cls, key):
                if key == "DEFAULT_UPLOAD" and value != "gd":
                    value = "rc"
                elif key in [
                    "BASE_URL",
                    "RCLONE_SERVE_URL",
                    "INDEX_URL",
                    "SEARCH_API_LINK",
                    "KUMA_URL",
                ]:
                    if value:
                        value = value.strip("/")
                elif key == "USENET_SERVERS":
                    try:
                        if not value[0].get("host"):
                            value = []
                    except Exception:
                        value = []
                value = cls._convert_env_type(key, value)
                setattr(cls, key, value)
        for key in ["BOT_TOKEN", "OWNER_ID", "TELEGRAM_API", "TELEGRAM_HASH"]:
            value = getattr(cls, key)
            if isinstance(value, str):
                value = value.strip()
            if not value:
                raise ValueError(f"{key} variable is missing!")


class BinConfig:
    ARIA2_NAME = bin_name(0)
    QBIT_NAME = bin_name(1)
    FFMPEG_NAME = bin_name(2)
    RCLONE_NAME = bin_name(3)
    SABNZBD_NAME = bin_name(4)
