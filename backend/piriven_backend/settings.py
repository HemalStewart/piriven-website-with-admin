import os
from pathlib import Path

# =========================
# Base Directory
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent

# =========================
# Security / Environment
# =========================
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "change-me-unsafe-secret-key")
DEBUG = os.getenv("DJANGO_DEBUG", "True") == "True"

# Allowed hosts
# - Remove any scheme (http/https), only use domain or IP
_raw_hosts = os.getenv("DJANGO_ALLOWED_HOSTS", "122.255.40.206,piriven.moe.gov.lk")
ALLOWED_HOSTS = [h.strip() for h in _raw_hosts.split(",") if h.strip()]

# =========================
# Installed Apps
# =========================
INSTALLED_APPS = [
    "jazzmin",  # Admin theme, must come before django.contrib.admin
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    # Third-party
    "rest_framework",
    "corsheaders",
    "django_filters",

    # Local apps
    "apps.content",
]

# =========================
# Middleware
# =========================
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # high priority
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "piriven_backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "piriven_backend.wsgi.application"

# =========================
# Database
# =========================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",  # dev only
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# =========================
# Password Validators
# =========================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# =========================
# Internationalization
# =========================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# =========================
# Static & Media
# =========================
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = [BASE_DIR / "assets"]  # dev-only assets

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# =========================
# REST Framework
# =========================
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "PAGE_SIZE_QUERY_PARAM": "page_size",
}

# =========================
# CORS / CSRF
# =========================
# For dev: Next.js frontend running locally
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

# Add public server IP for testing in dev (HTTP only)
if DEBUG:
    CORS_ALLOWED_ORIGINS.append("http://122.255.40.206:8000")

CORS_ALLOW_CREDENTIALS = True

# CSRF trusted origins
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]

if DEBUG:
    CSRF_TRUSTED_ORIGINS.append("http://122.255.40.206:8000")

# =========================
# Jazzmin Admin Customization
# =========================
JAZZMIN_SETTINGS = {
    "site_title": "Admin",
    "site_header": "Admin",
    "site_brand": "Admin",
    "welcome_sign": "Site Content Management",
    "site_logo": None,
    "site_icon": None,
    "copyright": "",
    "search_model": "content.News",
    "show_ui_builder": False,
    "related_modal_active": True,
    "topmenu_links": [
        {"name": "Dashboard", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Site", "url": "/", "new_window": True},
    ],
    "usermenu_links": [
        {"name": "View site", "url": "/", "new_window": True},
    ],
    "icons": {
        "apps.content": "fas fa-layer-group",
        "content.Album": "fas fa-images",
        "content.GalleryImage": "far fa-image",
        "content.News": "far fa-newspaper",
        "content.Notice": "fas fa-bullhorn",
        "content.Publication": "fas fa-download",
        "content.DownloadCategory": "fas fa-folder-open",
        "content.Video": "fas fa-video",
        "content.Event": "far fa-calendar-alt",
        "content.Stat": "fas fa-chart-bar",
        "content.ExternalLink": "fas fa-link",
        "content.HeroSlide": "fas fa-photo-video",
        "content.NewsletterSubscription": "far fa-envelope",
        "library.PublicationEntry": "fas fa-book",
        "library.PublicationCategory": "fas fa-book-open",
        "auth.User": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    "custom_css": "admin/custom.css",
    "custom_js": ["admin/custom.js"],
    "custom_links": {
        "content.News": [
            {
                "name": "View on site",
                "url": "/",
                "icon": "fas fa-external-link-alt",
                "new_window": True,
            }
        ]
    },
    "hide_apps": [],
    "hide_models": [],
}

JAZZMIN_UI_TWEAKS = {
    "theme": "flatly",
    "dark_mode_theme": None,
    "navbar": "navbar-dark bg-black",
    "sidebar": "sidebar-dark-danger",
    "brand_colour": "navbar-dark bg-black",
    "accent": "danger",
    "actions_sticky_top": True,
    "button_classes": {
        "primary": "btn btn-danger",
        "secondary": "btn btn-outline-secondary",
        "success": "btn btn-success",
        "warning": "btn btn-warning",
        "info": "btn btn-info",
        "danger": "btn btn-outline-danger",
    },
}
