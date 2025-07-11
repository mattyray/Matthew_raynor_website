from django.db import models
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex

# We'll add search vectors to existing models in migrations
# No models needed in this file for Phase 1