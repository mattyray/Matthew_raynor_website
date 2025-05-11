from .base import *

DEBUG = False
SECRET_KEY = "test-secret-key"

STRIPE_PUBLISHABLE_KEY = "pk_test_dummy"
STRIPE_SECRET_KEY = "sk_test_dummy"
STRIPE_WEBHOOK_SECRET = "whsec_dummy"

stripe.api_key = STRIPE_SECRET_KEY

# Use in-memory SQLite for faster tests
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "test.sqlite3",
    }
}

EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
RECAPTCHA_PUBLIC_KEY = "test"
RECAPTCHA_PRIVATE_KEY = "test"

# Add to test.py
GOOGLE_CLIENT_ID = "test-client-id"
GOOGLE_CLIENT_SECRET = "test-client-secret"

SOCIALACCOUNT_PROVIDERS['google']['APP']['client_id'] = GOOGLE_CLIENT_ID
SOCIALACCOUNT_PROVIDERS['google']['APP']['secret'] = GOOGLE_CLIENT_SECRET
