from .base import *

DEBUG = False
SECRET_KEY = "test-secret-key"

STRIPE_PUBLISHABLE_KEY = "pk_test_dummy"
STRIPE_SECRET_KEY = "sk_test_dummy"
STRIPE_WEBHOOK_SECRET = "whsec_dummy"
stripe.api_key = STRIPE_SECRET_KEY

# In-memory test DB
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "test.sqlite3",
    }
}

EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
RECAPTCHA_PUBLIC_KEY = "test"
RECAPTCHA_PRIVATE_KEY = "test"

# 👇 Google SSO override here only for tests
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
        'OAUTH_PKCE_ENABLED': True,
        'APP': {
            'client_id': 'test-client-id',
            'secret': 'test-secret',
            'key': ''
        }
    }
}
