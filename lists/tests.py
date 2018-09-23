from django.test import TestCase


class SmokeTest(TestCase):
    """
    The `TestCase` class is actually an extended verison of unittest.TestCase.
    It has Django specific features. Let's find out later.
    """
    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)

