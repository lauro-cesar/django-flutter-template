from django.test import TestCase
from accounts import signals


class BaseSignalSetup:
    @classmethod
    def setUpTestData(cls):
        cls.username = "demo"
        cls.password = "demo@2020"

    def setUp(self):
        self.pre_signals = (len(signals.post_save.receivers),)

    def tearDown(self):
        post_signals = (len(signals.post_save.receivers),)
        self.assertEqual(self.pre_signals, post_signals)


class SignalTests(BaseSignalSetup, TestCase):
    def test_save_signals(self):
        data = []

        def post_save_handler(signal, sender, instance, **kwargs):
            data.append(
                (instance, sender, kwargs.get("created"), kwargs.get("raw", False))
            )

        signals.post_save.connect(post_save_handler, weak=False)
        try:
            data[:] = []
        finally:
            signals.post_save.disconnect(post_save_handler)
