# Aplikace v Djangu (šablona WonderHost)

Kniha návštěv v [Djangu](https://www.djangoproject.com) s databází PostgreSQL
a českou administrací. Slouží jako začátek vlastní aplikace.

## Na hostingu WonderHost

Panel projektu připraví databázi a předá ji v proměnné `DATABASE_URL`. Každé nasazení
nainstaluje balíčky z `requirements.txt`, spustí `collectstatic` a migrace databáze
a aplikaci spustí přes gunicorn.

**Přístup do administrace (`/admin/`):** v panelu u projektu nastavte proměnné
`DJANGO_SUPERUSER_USERNAME` a `DJANGO_SUPERUSER_PASSWORD` a nasaďte projekt znovu.
Správce se založí při migraci. Heslo si pak můžete změnit v administraci
a proměnné smazat.

Další proměnné (nepovinné): `SECRET_KEY` (jinak se odvodí z přístupu k databázi),
`CSRF_TRUSTED_ORIGINS` (například `https://www.mojefirma.cz`, když formuláře hlásí chybu CSRF).

## Na počítači

```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
DJANGO_DEBUG=1 python manage.py migrate
DJANGO_DEBUG=1 python manage.py runserver
```

Bez `DATABASE_URL` se na počítači použije SQLite.
