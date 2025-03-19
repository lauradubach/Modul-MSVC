# Microservices - Flask mit Datenbank

## Technologien

- Flask (https://flask.palletsprojects.com/en/3.0.x/)
- ApiFlask (https://apiflask.com/)
- SQLAlchemy (https://www.sqlalchemy.org/)
- mySQL (https://www.mysql.com/de/)
- Docker Compose (https://docs.docker.com/compose/)

## Zweck

Dies ist eine Beispielapplikation für einen dockerized Flask-Server mit einer Anbindung an eine SQL Datenbank.

Es sollen Konzepte demonstriert werden, mit denen man Persistenz in Microservices herstellen kann.

Der Source Code ist ausschliesslich für Entwicklungszwecke gedacht.


## Funktionen

- Studenten und Kurse mit CRUD verwalten
- Studenten auf Kurse registrieren
- Alle Studenten eines Kurses anzeigen

## Installation

klone dieses Repo und wechsle in das Verzeichnis mit der Datei compose.yaml

führe folgenden Befehl aus:

```bash
docker compose up
```

## Lizenz

© 2024. This work is openly licensed via [CC BY-NC.SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
