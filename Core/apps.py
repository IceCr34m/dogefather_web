from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'Core'

    def ready(self):
        from Core import priceUpdater
        priceUpdater.start()
