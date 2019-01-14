# README

## Allgemeine Informationen

* Diese Django App dient der visualisierung eines Jahreskalenders mit Feiertagen und Schulferien.
* Das ganze ist noch in einer fr�hen Entwicklungsstufe

## Installation

Ben�tigt wird eine virtuelle Python3 Umgebung und eine PostgreSQL-Datenbank

* Ben�tigte Python Pakete:
    * django
    * psycopg2
    * django-extensions
    * holidays
* Optionale Pakete (Entwicklung):
    * django-debug-toolbar

Einrichten mit:
  
```console
$ pipenv install --dev
$ pipenv shell
```
  
Die Datenbank und einen entsprechenden User anlegen:

```console
$ sudo -u postgres createuser -d -P kalender
$ sudo -u postgres createdb -O kalender kalender
```

