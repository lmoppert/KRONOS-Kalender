# README

## Allgemeine Informationen

Diese Django App dient der Visualisierung eines Jahreskalenders mit Feiertagen
und Schulferien. Das ganze ist noch in einer frühen Entwicklungsstufe. 

## Installation

Benötigt wird eine virtuelle Python3 Umgebung und eine PostgreSQL-Datenbank

### Datenbank

Die Datenbank erstellen und einen entsprechenden User anlegen:

```console
$ sudo -u postgres createuser -d -P kalender
$ sudo -u postgres createdb -O kalender kalender
```

### Python

Die Benötigte Python Pakete sind im Pipfile hinterlegt:

  * django
  * psycopg2
  * django-extensions
  * holidays
  * dev: django-debug-toolbar

Installation der Pakete mit pipenv, aktivieren der Umgebung und initialisieren
der Anwendung:  

```console
$ pipenv install --dev
$ pipenv shell
$ python3 manage.py migrate
$ python3 manage.py compilemessages
```
