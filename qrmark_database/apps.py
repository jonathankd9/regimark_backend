from django.apps import AppConfig


class QrmarkDatabaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'qrmark_database'

    def ready(self):
        import qrmark_database.signals