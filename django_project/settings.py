from environ import Env
from pathlib import Path
import os

# Initialize environment variables
env = Env()
Env.read_env()

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# ✅ Security settings
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")  # Required for Heroku

# Secret Key & Debug Mode
SECRET_KEY = env("DJANGO_SECRET_KEY", default="No Secret Key Found")
DEBUG = env.bool("DJANGO_DEBUG", default=False)

# ✅ Allowed Hosts
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=[
    "localhost",
    "127.0.0.1",
    "matthew-raynor-site-3d5f17c6a796.herokuapp.com",
    "matthewraynor.com",
    "www.matthewraynor.com",
])


# ✅ Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
   # 'django.contrib.sites',  


    # Custom apps
    'accounts.apps.AccountsConfig',
    'pages.apps.PagesConfig',
    'store.apps.StoreConfig',
    'blog.apps.BlogConfig',
    'portfolio.apps.PortfolioConfig',



    # Third-party packages
    'crispy_forms',
    'crispy_bootstrap5',
    'import_export',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'embed_video',
    'django_recaptcha',


]

# ✅ Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'allauth.account.middleware.AccountMiddleware',  # Add this line
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ✅ URL Configuration
ROOT_URLCONF = 'django_project.urls'

# ✅ Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Include custom templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ✅ WSGI Application
WSGI_APPLICATION = 'django_project.wsgi.application'

# ✅ Database Configuration
DATABASES = {
    "default": env.db_url("DATABASE_URL")
}


# ✅ Authentication
AUTH_USER_MODEL = 'accounts.CustomUser'

# ✅ Password Validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ✅ Localization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]  # 👈 crucial for collectstatic to find non-app static files
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ✅ Default Primary Key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ✅ Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# ✅ Login & Logout
 

# ✅ Security Settings for Production
if not DEBUG:
    SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)
    SECURE_HSTS_SECONDS = env.int("DJANGO_SECURE_HSTS_SECONDS", default=2592000)  # 30 days
    SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool("DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True)
    SECURE_HSTS_PRELOAD = env.bool("DJANGO_SECURE_HSTS_PRELOAD", default=True)
    SESSION_COOKIE_SECURE = env.bool("DJANGO_SESSION_COOKIE_SECURE", default=True)
    CSRF_COOKIE_SECURE = env.bool("DJANGO_CSRF_COOKIE_SECURE", default=True)
else:
    SECURE_SSL_REDIRECT = False
    SECURE_HSTS_SECONDS = 0
    SECURE_HSTS_INCLUDE_SUBDOMAINS = False
    SECURE_HSTS_PRELOAD = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False


STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

IMPORT_EXPORT_USE_TRANSACTIONS = True
SITE_ID = 1


ACCOUNT_LOGIN_METHODS = {'email'}
ACCOUNT_SIGNUP_FIELDS = ['email*', 'password1*', 'password2*']
ACCOUNT_USER_MODEL_USERNAME_FIELD = "email"



ACCOUNT_EMAIL_VERIFICATION = 'optional'  # or 'optional' based on your preference
LOGIN_REDIRECT_URL = '/'  # or wherever you want to redirect after login
ACCOUNT_LOGOUT_REDIRECT_URL = '/'

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = "/" 

#Django recapctha

SILENCED_SYSTEM_CHECKS = ['django_recaptcha.recaptcha_test_key_error']


RECAPTCHA_PUBLIC_KEY = env("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = env("RECAPTCHA_PRIVATE_KEY")