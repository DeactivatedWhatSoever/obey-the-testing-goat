from django.test import TestCase
from django.urls import resolve
from lists.views import home_page


class SmokeTest(TestCase):
    """
    The `TestCase` class is actually an extended verison of unittest.TestCase.
    It has Django specific features. Let's find out later.
    """
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

