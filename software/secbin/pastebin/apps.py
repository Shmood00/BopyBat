from django.apps import AppConfig


class PastebinConfig(AppConfig):
    name = 'pastebin'

    def ready(self):
        import pastebin.signals