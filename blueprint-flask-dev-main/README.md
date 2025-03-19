# Microservices - Skalierbare Strukturen

## Technologien

- Flask (https://flask.palletsprojects.com/en/3.0.x/)
- ApiFlask (https://apiflask.com/)
- SQLAlchemy (https://www.sqlalchemy.org/)
- mySQL (https://www.mysql.com/de/)
- Docker Compose (https://docs.docker.com/compose/)

## Zweck

Dies ist eine Beispielapplikation für einen dockerized Flask-Server mit einer erweiterbaren Struktur.

Es sollen Konzepte demonstriert werden, mit denen man über Flask Blueprints und einer best-practice File-Struktur einen erweiterbaren Microservices erstellen kann.

Der Source Code ist ausschliesslich für Entwicklungszwecke gedacht.

Die abgeleitete Struktur wurde inspiriert von diesem [Digital Ocean Blog](https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy)

## Funktionen

- Studenten und Kurse mit CRUD verwalten
- Studenten auf Kurse registrieren
- Kurse mit Studenten verknüpfen
- Alle Studenten eines Kurses anzeigen
- Alle Kurse eines Studenten anzeigen

## Installation

klone dieses Repo und wechsle in das Verzeichnis mit der Datei compose.yaml

führe folgenden Befehl aus:

```bash
docker compose up
```

## Lizenz

© 2024. This work is openly licensed via [CC BY-NC.SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
