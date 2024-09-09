import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-+6_wtkz^6l!88xben4zu7+=p4h!_s3_2s7i-1k((7t+y6u*obj"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # apps
    "account.apps.AccountConfig",
    "home.apps.HomeConfig",
    "projects.apps.ProjectsConfig",
    "Feedback.apps.FeedbackConfig",
    # packages
    "fontawesomefree",
    "django_cleanup",
]

# packages
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "crowdfunding.urls"

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

WSGI_APPLICATION = "crowdfunding.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        # "ENGINE": "django.db.backends.sqlite3",
        # "NAME": BASE_DIR / "db.sqlite3",
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "crowd_funding",
        "USER": "django_proj",
        "PASSWORD": "django@@1",
        "HOST": "localhost",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = ["static/"]

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

# Email settings
AUTH_USER_MODEL = "account.User"

# django project
# xckz zfki waip vhoq

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "m9ee9m@gmail.com"
EMAIL_HOST_PASSWORD = "xckz zfki waip vhoq"

AUTHENTICATION_BACKENDS = (
    "social_core.backends.github.GithubOAuth2",  # github <----
    "social_core.backends.twitter.TwitterOAuth",  # twitter <----
    "social_core.backends.facebook.FacebookOAuth2",  # facebook <----
    "social_core.backends.google.GoogleOAuth2",  # google <----
    "django.contrib.auth.backends.ModelBackend",
)

SITE_ID = 1
SOCIAL_AUTH_GITHUB_KEY = "40d06a2a3d0d62d74dbd"
SOCIAL_AUTH_GITHUB_SECRET = "3c725f49cb9edf369b33b23c1ecf9b3d9bc95cdc"
SOCIAL_AUTH_LOGIN_REDIRECT_URL = "index"
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = (
    "534268798718-451t7sn6c7iuu8ts9jqvbhjtalg2vqa4.apps.googleusercontent.com"
)
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "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"
SOCIAL_AUTH_FACEBOOK_KEY = "3738217359745570"
SOCIAL_AUTH_FACEBOOK_SECRET = "7fdf8462e923299f9b618e46656fd6b9"

SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    "https://www.googleapis.com/auth/userinfo.email",
]
SOCIAL_AUTH_GITHUB_SCOPE = ["user:email"]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
