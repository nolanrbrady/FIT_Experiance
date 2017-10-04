import os
from urllib.parse import urlparse
import portal.secrets as secrets


FIT_ALLOW_ANONYMOUS = False

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))
BASE_DIR = PACKAGE_ROOT

DEBUG = True

dburl = urlparse(os.environ.get(
    'DATABASE_URL',
    secrets.DATABASE_URL
))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': dburl.path[1:] or '',
        'USER': dburl.username or '',
        'PASSWORD': dburl.password or '',
        'HOST': dburl.hostname or '',
        'PORT': dburl.port or '',
    }
}

ALLOWED_HOSTS = [
    "localhost","dev.thefitexperience.com","thefitexperience.com"
]

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "UTC"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

SITE_ID = int(os.environ.get("SITE_ID", 1))

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.environ.get('DJANGO_MEDIA_ROOT',os.path.join(PACKAGE_ROOT, "site_media", "media"))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = "/media/"

# Absolute path to the directory static files should be collected to.
# Don"t put anything in this directory yourself; store your static files
# in apps" "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
#STATIC_ROOT = os.path.join(PACKAGE_ROOT, "site_media", "static")
STATIC_ROOT = os.environ.get('DJANGO_STATIC_ROOT',os.path.join(PACKAGE_ROOT, "site_media", "static"))

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
#STATIC_URL = "/site_media/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, "static", "dist"),
]

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Make this unique, and don't share it with anybody.
SECRET_KEY = "SECRET_KEY REMOVED"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PACKAGE_ROOT, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "debug": DEBUG,
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.template.context_processors.request",
                "django.contrib.messages.context_processors.messages",
                "account.context_processors.account",
                "pinax_theme_bootstrap.context_processors.theme",
                "social.apps.django_app.context_processors.backends",
                "social.apps.django_app.context_processors.login_redirect",
            ],
        },
    },
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.SessionAuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "portal.urls"

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = "portal.wsgi.application"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.staticfiles",

    # theme
    "bootstrapform",
    "pinax_theme_bootstrap",

    # externa
    "account",
    "haystack",
    "rest_framework",
    "pinax.eventlog",
    "pinax.webanalytics",
    "social.apps.django_app.default",

    # project
    "portal",
    "portal.core.fit",
]

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
        },
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler"
        }
    },
    "loggers": {
        "fit": {
            "handlers": ["console"],
            "level": 'DEBUG',
            "propagate": False,
        },
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        #"django.db.backends": {
        #    "handlers": ["console"],
        #    "level": "DEBUG",
        #},
    }
}

FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER='fit-dev'
EMAIL_HOST_PASSWORD='EMAIL_HOST_PASSWORD REMOVED'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

#EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DEFAULT_FROM_EMAIL = 'Pete@TheFitExperience.com'

THEME_CONTACT_EMAIL = 'Pete@TheFitExperience.com'

ACCOUNT_SOCIAL_AUTH = True
ACCOUNT_OPEN_SIGNUP = secrets.ACCOUNT_OPEN_SIGNUP
ACCOUNT_EMAIL_UNIQUE = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = True
ACCOUNT_LOGIN_REDIRECT_URL = LOGIN_REDIRECT_URL = "home"
ACCOUNT_LOGOUT_REDIRECT_URL = "home"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_USE_AUTH_AUTHENTICATE = True
ACCOUNT_LOGOUT_ON_GET = True

ACCOUNT_USER_DISPLAY = lambda user: user.email
# Elsewhere, use the following:
#    from account.utils import user_display
#    user_display(user)
# Or in templates:
#   {% load account_tags %}
#   {% user_display request.user %}
#

AUTHENTICATION_BACKENDS = [
    "social.backends.google.GoogleOAuth2",
    "account.auth_backends.EmailAuthenticationBackend",
    #"account.auth_backends.UsernameAuthenticationBackend",
]

SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True

# FIXME kill these and regenerate - https://console.developers.google.com/apis/credentials/oauthclient/
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''

SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''

SOCIAL_AUTH_URL_NAMESPACE = 'social'

SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username','email']

LOGIN_URL = '/account/login/'

LOGOUT_REDIRECT_URL = '/'

# Mixpanel keys
MIXPANEL_TOKEN = os.environ.get('MIXPANEL_TOKEN', secrets.MIXPANEL_TOKEN)
MIXPANEL_SECRET = os.environ.get('MIXPANEL_SECRET', secrets.MIXPANEL_SECRET)

SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY', secrets.SENDGRID_API_KEY)


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}
