from django.test import TestCase


class SmokeTest(TestCase):
    """
    The `TestCase` class is actually an extended verison of unittest.TestCase.
    It has Django specific features. Let's find out later.
    """
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={ 'item_text': 'A new list item' })
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')

