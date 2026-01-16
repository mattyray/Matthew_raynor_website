from environ import Env
from pathlib import Path
print("💥 settings.py loaded from latest build")

# Initialize environment variables
env = Env()
Env.read_env()

OPENAI_API_KEY = env("OPENAI_API_KEY", default="")

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Security
SECRET_KEY = env("DJANGO_SECRET_KEY", default="No Secret Key Found")
DEBUG = env.bool("DJANGO_DEBUG", default=False)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Allowed hosts
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=[
    "localhost",
    "127.0.0.1",
    "0.0.0.0",
    "web",
    "matthew-raynor-site-3d5f17c6a796.herokuapp.com",
    "matthewraynor.com",
    "www.matthewraynor.com",
])

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',

    # Custom apps
    'accounts.apps.AccountsConfig',
    'pages.apps.PagesConfig',
    'store.apps.StoreConfig',
    'blog.apps.BlogConfig',
    'portfolio.apps.PortfolioConfig',
    'chat.apps.ChatConfig',
    'search.apps.SearchConfig',  # <-- ADD THIS LINE


    # Third-party
    'django.contrib.sites',
    'crispy_forms',
    'crispy_bootstrap5',
    'import_export',
    'embed_video',
    'django_recaptcha',
    'django_extensions',
    'ckeditor',
    'ckeditor_uploader',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL config
ROOT_URLCONF = 'django_project.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.parent / 'templates'],
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

WSGI_APPLICATION = 'django_project.wsgi.application'

# Database
DATABASES = {
    "default": env.db_url("DATABASE_URL")
}

# Authentication
AUTH_USER_MODEL = 'accounts.CustomUser'
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# Required for django.contrib.sites
SITE_ID = env.int("DJANGO_SITE_ID", default=1)

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Localization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR.parent / "static"]
STATIC_ROOT = BASE_DIR.parent / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Media (Cloudinary) - ENHANCED WITH OPTIMIZATION
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# NEW: Cloudinary optimization settings
CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': env('CLOUDINARY_URL', default=''),
    'TRANSFORMATION': {
        'quality': 'auto:good',
        'fetch_format': 'auto', 
        'flags': 'progressive',
    }
}

# Staticfiles finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# reCAPTCHA
SILENCED_SYSTEM_CHECKS = ['django_recaptcha.recaptcha_test_key_error']
RECAPTCHA_PUBLIC_KEY = env("RECAPTCHA_PUBLIC_KEY", default="test")
RECAPTCHA_PRIVATE_KEY = env("RECAPTCHA_PRIVATE_KEY", default="test")

# Email
EMAIL_BACKEND = env("EMAIL_BACKEND", default="django.core.mail.backends.locmem.EmailBackend")
EMAIL_HOST = env("EMAIL_HOST", default="smtp.test.com")
EMAIL_PORT = env.int("EMAIL_PORT", default=587)
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=True)
EMAIL_HOST_USER = env("EMAIL_HOST_USER", default="test@test.com")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default="testpassword")
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL", default="noreply@test.com")

# Production security
if not DEBUG:
    SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)
    SECURE_HSTS_SECONDS = env.int("DJANGO_SECURE_HSTS_SECONDS", default=2592000)
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

# Import-export
IMPORT_EXPORT_USE_TRANSACTIONS = True

# Auto field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
        'height': 300,
        'width': 'auto',
        'extraPlugins': ','.join([
            'uploadimage', 'image2', 'embed', 'autoembed', 'codesnippet',
        ]),
    }
}