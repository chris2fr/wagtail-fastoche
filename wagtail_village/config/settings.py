"""
Django settings for wagtail_village project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/

Inspiration
https://github.com/betagouv/tous-a-bord/blob/main/config/settings.py
"""

import os
from pathlib import Path

import dj_database_url
from dotenv import load_dotenv


load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if os.getenv("DEBUG") == "True" else False
DEBUG_TOOLBAR = True if os.getenv("DEBUG_TOOLBAR") == "True" else False


ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "127.0.0.1, localhost").replace(" ", "").split(",")

HOST_URL = os.getenv("HOST_URL", "localhost")

# Application definition

INSTALLED_APPS = [
    "storages",
    "wagtail.contrib.redirects",
    "wagtail.contrib.settings",
    "wagtail.contrib.forms",
    # 'wagtail.wagtailforms',
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.admin",
    "wagtail.search",
    "wagtail.snippets",
    "wagtail",
    "wagtailmarkdown",
    "wagtailmenus",
    "wagtail_localize",
    "wagtail_localize.locales",
    "taggit",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "widget_tweaks",
    "django_village.theme_lesgrandsvoisins",
    "django_village.theme_designsystem",
    "django_village",
    "sass_processor",
    "wagtail_village",
    "wagtail_village_dashboard",
    "wagtail_village_blog",
    "wagtail_village_lesgrandsvoisins",
    "wagtail_village_forms",
]

# Only add these on a dev machine
# if DEBUG and "localhost" in HOST_URL:
if DEBUG:
    INSTALLED_APPS += [
        "django_extensions",
        "wagtail.contrib.styleguide",
    ]

if DEBUG_TOOLBAR:
    INSTALLED_APPS += [
        "debug_toolbar",
    ]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

# if DEBUG and "localhost" in HOST_URL:
if DEBUG_TOOLBAR:
    MIDDLEWARE += [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]

ROOT_URLCONF = "wagtail_village.config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "django_village/templates"),
            os.path.join(BASE_DIR, "wagtail_village/templates"),
            os.path.join(BASE_DIR, "wagtail_village_blog/templates"),
            os.path.join(BASE_DIR, "wagtail_village_dashbord/templates"),
            os.path.join(BASE_DIR, "wagtail_village_forms/templates"),
            os.path.join(BASE_DIR, "wagtail_village_lesgrandsvoisins/templates"),
            os.path.join(BASE_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "wagtail.contrib.settings.context_processors.settings",
                "wagtailmenus.context_processors.wagtailmenus",
                "django_village.context_processors.site_config",
                "wagtail_village.context_processors.skiplinks",
                "wagtail_village.context_processors.mega_menus",
                "wagtail_village.context_processors.urlangs",
                "wagtail_village.context_processors.sitevars",
            ],
        },
    },
]

WSGI_APPLICATION = "wagtail_village.config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL:
    DATABASES = {
        "default": dj_database_url.parse(
            DATABASE_URL,
            conn_max_age=600,
            conn_health_checks=True,
        )
    }
else:
    raise ValueError("Please set the DATABASE_URL environment variable")

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

WAGTAIL_PASSWORD_RESET_ENABLED = os.getenv("WAGTAIL_PASSWORD_RESET_ENABLED", False)


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "fr"

TIME_ZONE = "Europe/Paris"

USE_I18N = True

USE_L10N = True

USE_TZ = True

WAGTAIL_I18N_ENABLED = True

WAGTAIL_CONTENT_LANGUAGES = LANGUAGES = [
    ("en", "English"),
    ("fr", "French"),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STORAGES = {}
STORAGES["staticfiles"] = {
    "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
}

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "sass_processor.finders.CssFinder",
]

# S3 uploads & MEDIA CONFIGURATION
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html

if os.getenv("S3_HOST"):
    endpoint_url = f"{os.getenv('S3_PROTOCOL', 'https')}://{os.getenv('S3_HOST')}"

    STORAGES["default"] = {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "bucket_name": os.getenv("S3_BUCKET_NAME", "set-bucket-name"),
            "access_key": os.getenv("S3_KEY_ID", "123"),
            "secret_key": os.getenv("S3_KEY_SECRET", "secret"),
            "endpoint_url": endpoint_url,
            "region_name": os.getenv("S3_BUCKET_REGION", "fr"),
            "file_overwrite": False,
            "location": os.getenv("S3_LOCATION", ""),
        },
    }

    MEDIA_URL = f"{endpoint_url}/"
else:
    STORAGES["default"] = {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    }
    MEDIA_URL = "/medias/"
    MEDIA_ROOT = os.path.join(BASE_DIR, os.getenv("MEDIA_ROOT", ""))

# Django Sass
SASS_PROCESSOR_ROOT = os.path.join(BASE_DIR, "static/css")
SASS_PROCESSOR_AUTO_INCLUDE = False

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# Wagtail settings
# https://docs.wagtail.org/en/stable/reference/settings.html

WAGTAIL_SITE_NAME = os.getenv("SITE_NAME", "Sites faciles")

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = f"{os.getenv('HOST_PROTO', 'https')}://{HOST_URL}"

HOST_PORT = os.getenv("HOST_PORT", "")
if HOST_PORT != "":
    WAGTAILADMIN_BASE_URL = f"{WAGTAILADMIN_BASE_URL}:{HOST_PORT}"

# Disable Gravatar service
WAGTAIL_GRAVATAR_PROVIDER_URL = None

WAGTAIL_RICHTEXT_FIELD_FEATURES = [
    "h2",
    "h3",
    "h4",
    "bold",
    "italic",
    "link",
    "document-link",
    "image",
    "embed",
]

WAGTAILEMBEDS_RESPONSIVE_HTML = True
WAGTAIL_MODERATION_ENABLED = False
WAGTAILMENUS_FLAT_MENUS_HANDLE_CHOICES = (
    ("header_tools", "Menu en haut à droite"),
    ("footer", "Menu en pied de page"),
    ("mega_menu_section_1", "Catégorie de méga-menu 1"),
    ("mega_menu_section_2", "Catégorie de méga-menu 2"),
    ("mega_menu_section_3", "Catégorie de méga-menu 3"),
    ("mega_menu_section_4", "Catégorie de méga-menu 4"),
    ("mega_menu_section_5", "Catégorie de méga-menu 5"),
    ("mega_menu_section_6", "Catégorie de méga-menu 6"),
    ("mega_menu_section_7", "Catégorie de méga-menu 7"),
    ("mega_menu_section_8", "Catégorie de méga-menu 8"),
    ("mega_menu_section_9", "Catégorie de méga-menu 9"),
    ("mega_menu_section_10", "Catégorie de méga-menu 10"),
    ("mega_menu_section_11", "Catégorie de méga-menu 11"),
    ("mega_menu_section_12", "Catégorie de méga-menu 12"),
    ("mega_menu_section_13", "Catégorie de méga-menu 13"),
    ("mega_menu_section_14", "Catégorie de méga-menu 14"),
    ("mega_menu_section_15", "Catégorie de méga-menu 15"),
    ("mega_menu_section_16", "Catégorie de méga-menu 16"),
)

WAGTAILIMAGES_EXTENSIONS = ["gif", "jpg", "jpeg", "png", "webp", "svg"]

CSRF_TRUSTED_ORIGINS = []
for host in ALLOWED_HOSTS:
    CSRF_TRUSTED_ORIGINS.append("https://" + host)

SF_ALLOW_RAW_HTML_BLOCKS = os.getenv("SF_ALLOW_RAW_HTML_BLOCKS", "False").lower() == "true"

# if DEBUG and "localhost" in HOST_URL:
if DEBUG_TOOLBAR:
    INTERNAL_IPS = [
        "127.0.0.1",
        "0.0.0.0",
    ]
