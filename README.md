# scheduler_app

# Dependencies

- Python 3.7
    
    If you have some problems with `Ubuntu` and `sqlite3`, try `miniconda` https://docs.conda.io/en/latest/miniconda.html

Active the virtual environment:

```
. env/bin/activate
```

# Install

Install packages:

```
pip install -r requeriments.txt
```

```
cd scheduler
```

Populate a DB:

```
./manage.py migrate
python manage.py migrate
```

Run APP:

```
./manage.py runserver
python manage.py runserver
```

# Commands

Create admin:

```
./manage.py createsuperuser
```

Create an app inside this project:

```
./manage.py startapp appname
```
