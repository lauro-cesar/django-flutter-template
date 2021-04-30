from django.test import TestCase


class UserAccountTests(TestCase):
    """"""

    def test_user_model_importable(self):
        try:
            from accounts.models import User
        except Exception:
            self.fail()
