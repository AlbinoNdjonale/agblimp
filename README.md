# projetoAgbLimp

## Run project

### Installing the dependece

if you use pip

```bash
pip install -r requiremnts.txt
```

if you use poetry

```bash
poetry install
```

You can't use this method in production
```bash
python manage.py runserver
```

You can use this method in production
```bash
gunicor agblimp.wsgi:application
```

## Run test

```bash
python manage.py test
```