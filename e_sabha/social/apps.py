from django.apps import AppConfig


class SocialConfig(AppConfig):
    name = 'social'
    def ready(Self):
        import social.mysignal
