"""Nastavení projektu. Hodnoty, které se liší mezi počítačem a hostingem,
se čtou z proměnných prostředí (na WonderHostu je nastavíte u projektu)."""

import hashlib
import os
from pathlib import Path

import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# Databáze: na hostingu ji panel předá v DATABASE_URL, na počítači se
# použije SQLite.
DATABASE_URL = os.environ.get("DATABASE_URL", "")
DATABASES = {
    "default": dj_database_url.parse(DATABASE_URL, conn_max_age=60)
    if DATABASE_URL
    else {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "db.sqlite3"}
}

# DEBUG jen na počítači (DJANGO_DEBUG=1), na hostingu nikdy.
DEBUG = os.environ.get("DJANGO_DEBUG") == "1"

# Tajný klíč: vlastní z proměnné SECRET_KEY, jinak odvozený z přístupu
# k databázi (ten je tajný a pro projekt stálý).
SECRET_KEY = os.environ.get("SECRET_KEY") or (
    hashlib.sha256(("django:" + DATABASE_URL).encode()).hexdigest()
    if DATABASE_URL
    else "jen-pro-vyvoj-na-pocitaci"
)

# Požadavky přicházejí přes webserver hostingu, který propouští jen
# domény projektu.
ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = [
    o.strip() for o in os.environ.get("CSRF_TRUSTED_ORIGINS", "").split(",") if o.strip()
]
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "kniha",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "web.urls"
WSGI_APPLICATION = "web.wsgi.application"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "cs"
TIME_ZONE = "Europe/Prague"
USE_I18N = True
USE_TZ = True

# Statické soubory: hosting je po sestavení (collectstatic) zveřejní sám.
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
