from .base import *

DEBUG = True

# Use Stripe test key or fallback
STRIPE_PUBLISHABLE_KEY = env("STRIPE_PUBLISHABLE_KEY", default="pk_test_dummy")
STRIPE_SECRET_KEY = env("STRIPE_SECRET_KEY", default="sk_test_dummy")
STRIPE_WEBHOOK_SECRET = env("STRIPE_WEBHOOK_SECRET", default="whsec_dummy")

stripe.api_key = STRIPE_SECRET_KEY
