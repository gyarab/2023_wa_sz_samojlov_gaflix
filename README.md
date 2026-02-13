# 2023_wa_sa_samojlov_gaflix

Jedná se o webovou aplikaci Django, ve které si uživatel může přidávat a upravovat filmy.

[![Deployed on PythonAnywhere](https://img.shields.io/badge/deployed-on%20PythonAnywhere-brightgreen)](https://vlada.pythonanywhere.com/)

Inicializace projektu

```bash

# vytvorit venv a aktivovat
py -3 -m venv venv
source ./venv/Scripts/activate

# nainstalovat zavislosti
pip install -r requirements.txt
```

## Spuštění projektu

```
git pull
source ./venv/Scripts/activate
./manage.py migrate
./manage.py runserver
```

## Po změně `models.py`

```
./manage.py makemigrations
./manage.py migrate
```

## Reset databáze

```
# smazat aktualni DB
rm db.sqlite3

# obnovit strukturu
./manage.py migrate

# nahrat data
./manage.py loaddata fixtures/*.json
```
