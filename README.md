# Gaflix 🎬

Jedná se o responzivní webovou aplikaci vytvořenou ve frameworku Django, která uživateli zobrazuje přehled nejznámějších českých herců, režisérů a filmů. U každé osobnosti je uveden rok narození a základní informace. 

Filmy lze v aplikaci vyhledávat podle žánru nebo názvu pomocí vyhledávacího pole. U každého filmu je zobrazen název, stručný popis, žánry, herci, režiséři a rok uvedení. Po rozkliknutí detailu si uživatel může přečíst celý obsah filmu.

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
