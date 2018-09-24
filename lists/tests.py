from django.test import TestCase


class SmokeTest(TestCase):
    """
    The `TestCase` class is actually an extended verison of unittest.TestCase.
    It has Django specific features. Let's find out later.
    """
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

