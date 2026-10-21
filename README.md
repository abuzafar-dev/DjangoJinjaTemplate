# Django + Jinja2 Template

Django loyihasi, shablonlar Jinja2 orqali ishlaydi. Misol sifatida oddiy blog: postlarni qo'shish, ko'rish, tahrirlash va o'chirish.

## Quick start

```bash
make run     # creates .venv and .env, installs deps, starts the app
make test    # checks + tests
```

## Ishga tushirish

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

http://127.0.0.1:8000/

## Jinja2 sozlamasi

- `config/settings.py` ichida `TEMPLATES` ga `django.template.backends.jinja2.Jinja2` qo'shilgan
- `config/jinja2.py` da `static()`, `url()` va `get_messages()` funksiyalari global qilingan
- Admin panel Django shablonlari bilan ishlashda davom etadi

## Testlar

```bash
python manage.py test
```
