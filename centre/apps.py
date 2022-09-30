from django.apps import AppConfig


class CentreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'centre'

    def ready(self):
        import centre.signals
