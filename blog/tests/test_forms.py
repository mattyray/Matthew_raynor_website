from django.test import TestCase

class BlogModelsSmokeTest(TestCase):
    def test_smoke(self):
        # trivial test to verify blog app loads
        self.assertTrue(True)
