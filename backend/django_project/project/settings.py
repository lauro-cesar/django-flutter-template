"""
"""
from celery.schedules import crontab
import os
import firebase_admin
from firebase_admin import credentials

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUTH_USER_MODEL = "accounts.User"

FIREBASE_APP = firebase_admin.initialize_app()

redis_host = os.environ.get("REDIS_HOST", default="localhost")
cache_host = os.environ.get("CACHE_HOST", default="localhost")
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    default="_fake_key_",
)
DEBUG = int(os.environ.get("DEBUG", default=1))


CELERY_BROKER_URL = "redis://{redis}:6379".format(redis=redis_host)
CELERY_RESULT_BACKEND = "redis://{redis}:6379".format(redis=redis_host)


CELERY_ENABLE_UTC = True
CELERY_TIMEZONE = "America/Sao_Paulo"
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_SERIALIZER = "json"
TIME_ZONE = "America/Sao_Paulo"


REST_FRAMEWORK = {
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework_xml.parsers.XMLParser",
    ],
    # "EXCEPTION_HANDLER": "server.exception_handler.custom_exception_handler",
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {"anon": "1000/day", "user": "10000/day"},
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ],
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_PAGINATION_CLASS": "project.pagination.FlutterPagination",
    "PAGE_SIZE": 50,
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
}


SITE_ID = 1

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "django.localhost.hostcert.com.br",
    "[::1]",
]


API_VERSION = 1

ADMIN_TOOLS_INDEX_DASHBOARD = "project.dashboard.main.MainDashboard"
ADMIN_TOOLS_APP_INDEX_DASHBOARD = "project.dashboard.main.MainAppIndexDashboard"
ADMIN_TOOLS_MENU = "project.dashboard.menu.MainMenu"
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
APPEND_SLASH = True

INSTALLED_APPS = [
    "admin_tools",
    "admin_tools.theming",
    "admin_tools.menu",
    "admin_tools.dashboard",
    "project.apps.ProjectConfig",
    "rest_framework",
    "rest_framework.authtoken",
    "django_filters",
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.flatpages",
    "django.contrib.humanize",
]


SESSION_EXPIRE_AT_BROWSER_CLOSE = True

MIDDLEWARE = [
    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.flatpages.middleware.FlatpageFallbackMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
        ],
        "APP_DIRS": False,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
                "admin_tools.template_loaders.Loader",
            ],
        },
    }
]


CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "LOCATION": "localhost:11211",
        "TIMEOUT": 120,
        "OPTIONS": {"server_max_value_length": 1024 * 1024 * 100},
    }
}

WSGI_APPLICATION = "project.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", default="django.db.backends.postgresql"),
        "NAME": os.environ.get("PGDATABASE", default="django_db"),
        "USER": os.environ.get("PGUSER", default="django_user"),
        "PASSWORD": os.environ.get("PGPASSWORD", default="django_password"),
        "HOST": os.environ.get("PGHOSTADDR", default="127.0.0.1"),
        "PORT": os.environ.get("PGPORT", default="5432"),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "pt-br"
LANGUAGES = [("pt-br", "Português")]
TIME_ZONE = "UTC"
USE_I18N = True
USE_THOUSAND_SEPARATOR = True
USE_L10N = True
STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
STATIC_URL = "/static/"
MEDIA_URL = "/media/"
