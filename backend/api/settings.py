from pathlib import Path
import os
from api.constants import constants

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = constants.django_secret
DEBUG = constants.debug
ALLOWED_HOSTS = ["*"]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")


INSTALLED_APPS = [
    "rest_framework",
    "corsheaders",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [
    f"https://localhost:{constants.frontend_port}",
]
CORS_ALLOW_METHODS = [
    "GET",
]
ROOT_URLCONF = "api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "api.wsgi.application"


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


STATIC_URL = "static/"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
