import os
from pathlib import Path
from warnings import filterwarnings

from dotenv import load_dotenv

# ========================
# BASE DIR
# ========================
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)  # crée le dossier logs si inexistant

# ========================
# DOTENV
# ========================
load_dotenv(dotenv_path=BASE_DIR / ".env")

# ========================
# SECRET KEY / DEBUG
# ========================
SECRET_KEY = os.environ.get("SECRET_KEY", default="dev-secret-key-for-local")
DEBUG = os.environ.get("DEBUG", True)

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "localhost").split(" ")

# ========================
# APPS
# ========================
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
    "django.contrib.sites",
]

# THIRD_PARTY_APPS = []

# LOCAL_APPS = [
#    "apps",]

INSTALLED_APPS = DJANGO_APPS

# ========================
# MIDDLEWARE
# ========================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

# ========================
# TEMPLATES
# ========================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATES_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# ========================
# DATABASE
# ========================
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.postgresql"),
        "NAME": os.environ.get("SQL_DATABASE", "potion"),
        "USER": os.environ.get("SQL_USER", "potion"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "potion"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}

# ========================
# AUTH / ACCOUNTS
# ========================
# AUTH_USER_MODEL = "apps.User"
# AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)
DJANGO_SUPERUSER_PASSWORD = os.environ.get("DJANGO_SUPERUSER_PASSWORD")
# ========================
# STATIC
# ========================
STATIC_URL = "/static/"
if DEBUG:
    STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = BASE_DIR / "staticfiles"

# ========================
# LOGGING
# ========================
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": LOG_DIR / "django.log",
        },
    },
    "root": {
        "handlers": ["file"],
        "level": "DEBUG",
    },
}

# ========================
# AUTRES
# ========================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

filterwarnings(
    "ignore",
    "The FORMS_URLFIELD_ASSUME_HTTPS transitional setting is deprecated.",
)
FORMS_URLFIELD_ASSUME_HTTPS = True

SITE_ID = 1
