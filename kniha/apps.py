import os

from django.apps import AppConfig
from django.db.models.signals import post_migrate


def zalozit_spravce(sender, **kwargs):
    """Po každé migraci (tedy i po nasazení) založí správce administrace,
    když jsou nastavené proměnné DJANGO_SUPERUSER_USERNAME a
    DJANGO_SUPERUSER_PASSWORD a takový uživatel ještě není."""
    jmeno = os.environ.get("DJANGO_SUPERUSER_USERNAME", "").strip()
    heslo = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "")
    if not jmeno or not heslo:
        return
    from django.contrib.auth import get_user_model

    User = get_user_model()
    if not User.objects.filter(username=jmeno).exists():
        User.objects.create_superuser(jmeno, os.environ.get("DJANGO_SUPERUSER_EMAIL", ""), heslo)


class KnihaConfig(AppConfig):
    name = "kniha"
    verbose_name = "Kniha návštěv"

    def ready(self):
        post_migrate.connect(zalozit_spravce, sender=self)
