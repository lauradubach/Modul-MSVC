# Modul-MSVC

## Minimal Flask Server

https://gitlab.com/ch-tbz-wb/Stud/MSVC/-/blob/main/2_Unterrichtsressourcen/B_Microservices_lokal/01_minimal_dockerized_flask.md?ref_type=heads

Hier ist die Zusammenfassung im **Markdown-Format**:  


# Python und API-Entwicklung

Python ist eine vielseitige Programmiersprache, die sich besonders für die API-Entwicklung eignet. Beliebte Frameworks dafür sind **Django, Flask und FastAPI**:

- **Django**: Vollumfängliches Framework mit vielen integrierten Features.
- **Flask**: Minimalistisches Framework, das flexibel durch externe Bibliotheken erweitert werden kann.
- **FastAPI**: Moderne Lösung mit **Asynchronität** und **Typhinweisen**, besonders schnell.

Der Autor bevorzugt **Flask und FastAPI** und gibt Tipps zur API-Entwicklung mit Flask.

---

## Best Practices für API-Entwicklung

### 1. Klare und konsistente Endpunkt-Namen und HTTP-Verben

- **Ressourcen sollten als Plural-Nomen benannt werden** (z. B. `/users`, `/users/{userId}`).
- **Trennzeichen**:
  - **Bindestriche (`-`)** für bessere Lesbarkeit (`/users/{userId}/mobile-devices`).
  - **Schrägstriche (`/`)** zur Darstellung der Hierarchie.
  - **Kleinbuchstaben** für URLs.
- **CRUD-Operationen mit HTTP-Verben**:
  - `GET /users` → Liste aller Nutzer
  - `POST /users` → Neuen Nutzer erstellen
  - `PUT /users/{userId}` → Nutzer aktualisieren
  - `DELETE /users/{userId}` → Nutzer löschen
  - `PATCH /users/{userId}` → Teilweise Aktualisierung

🚫 **Falsch**:
`/users/get-all`, `/users/create`, `/users/{userId}/list-orders`.

---

### 2. Strukturierung der Anwendung

Es gibt keine feste Regel für den Aufbau einer Flask-Anwendung, aber eine bewährte Struktur ist:

```plaintext
project/
│── api/
│   ├── model/
│   ├── route/
│   ├── schema/
│   ├── service/
│── test/
│   ├── route/
│── app.py
│── Pipfile
│── .gitignore
```

- **Models**: Datenbeschreibungen (z. B. Datenbank-Modelle).
- **Routes**: Definiert API-Endpunkte.
- **Schemas**: Validierung der Eingaben/Ausgaben.
- **Services**: Geschäftslogik, um den Code in Routen schlank zu halten.

Blueprints helfen dabei, Routen zu organisieren:

```python
home_api = Blueprint('api', __name__, url_prefix='/home-service')
```

---

### 3. Automatische API-Dokumentation mit Swagger

Anstatt Dokumentation manuell zu schreiben, kann **Swagger** genutzt werden:

- **Flasgger** ist eine Bibliothek für Flask, die automatisch interaktive API-Dokumentation erstellt.
- **Swagger-Daten** werden aus Code-Kommentaren und `@swag_from` Annotationen bezogen.

```python
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Welcome message',
            'schema': WelcomeSchema
        }
    }
})
```

---

### 4. Test-Driven Development (TDD)

Tests sind wichtig für stabile APIs. **TDD (Test-Driven Development)** bedeutet:

1. **Test zuerst schreiben**:

    ```python
    def test_answer():
        assert sum_two_numbers(3, 5) == 8
    ```

2. **Code schreiben, damit der Test besteht**:

    ```python
    def sum_two_numbers(num1, num2):
        return num1 + num2
    ```

3. **Test ausführen** – Falls er fehlschlägt, Code korrigieren.

---

## Fazit

Es gibt nicht **die eine** richtige Methode für API-Entwicklung, aber **Konsistenz, Modularität, Dokumentation und Tests** sind essenziell.  
Durch die Befolgung dieser Best Practices kann man **effizienter APIs entwickeln und deren Qualität steigern**. 🚀

Dieses Markdown-Format kann direkt in einem Markdown-Editor oder GitHub verwendet werden.

# CRUD

Die CRUD-Operationen (Create, Read, Update, Delete) sind grundlegende Funktionen beim Aufbau von APIs, die es ermöglichen, Daten zu erstellen, abzurufen, zu aktualisieren und zu löschen. Diese vier Operationen sind oft notwendig, um ein vollständiges und benutzbares Modell zu schaffen. Wenn eine Aktion nicht durch eine dieser vier Operationen beschrieben werden kann, sollte sie möglicherweise als eigenes Modell betrachtet werden.

Im Zusammenhang mit REST-APIs entsprechen CRUD-Operationen oft den HTTP-Methoden POST (Create), GET (Read), PUT (Update) und DELETE (Delete). Dies sind fundamentale Elemente für ein persistenten Speichersystem.

Beispiel eines RESTful Systems für ein Restaurantmenü:
- Create: Um ein neues Gericht hinzuzufügen, wird eine POST-Anforderung verwendet. Der Server antwortet mit einem HTTP-Code 201 (Created).
- Read: Mit GET wird die gesamte Liste von Gerichten oder ein spezifisches Gericht abgerufen, ohne dass Daten verändert werden. Erfolgreiche Anfragen erhalten den Statuscode 200 (OK).
- Update: PUT wird verwendet, um ein Gericht zu aktualisieren, wie z. B. eine Preisänderung. Der Server antwortet mit 200 (OK).
- Delete: Mit DELETE wird ein Gericht aus dem Menü entfernt. Der Server antwortet mit 204 (No Content), ohne eine Antwort im Body zu liefern.

CRUD-Operationen bieten eine einfache und klare Struktur für die Entwicklung und Verwaltung von APIs und Datenbanken.

CRUD ist eine Abkürzung aus dem Datenmanagement und steht für die vier grundlegenden Operationen in Datenbanken: **Create** (Erstellen), **Read** (Lesen), **Update** (Aktualisieren) und **Delete** (Löschen). Diese Funktionen ermöglichen die Verwaltung von Daten in persistenten Datenbanken.

Einsatzzweck:
- Datenbank-Experten nutzen CRUD-Operationen, um Datenbankprobleme zu beheben oder Daten zu bereinigen.
- Endanwender verwenden CRUD, um beispielsweise Konten zu erstellen, zu ändern oder zu löschen.

CRUD dient auch als eine Checkliste für Entwickler, um sicherzustellen, dass ein Anwendungsmodell alle vier Operationen unterstützt. Wenn eine Aktion nicht durch CRUD beschrieben werden kann, sollte ein eigenes Modell entwickelt werden.

Sprachumgebungen: CRUD wird in verschiedenen Programmiersprachen und Plattformen verwendet, z. B. Java, JavaScript, PHP, .NET und Python. In SQL entsprechen die CRUD-Operationen den Befehlen `INSERT`, `SELECT`, `UPDATE` und `DELETE`. Bei RESTful HTTP sind es `POST`, `GET`, `PUT` und `DELETE`.

CRUD-Frameworks: Diese Frameworks ermöglichen es, Datenbankobjekte über eine grafische Oberfläche darzustellen und zu bearbeiten. Sie sind besonders in Mehrbenutzersystemen nützlich, da mehrere Benutzer gleichzeitig Daten einsehen können. 

Anwendungsbeispiel: Eine einfache Aufgabenlisten-App verwendet CRUD, um Aufgaben hinzuzufügen, anzuzeigen, zu ändern und zu löschen.

Nachteile und Grenzen: CRUD ist oft zu einfach, um komplexere Anforderungen abzubilden. Beispielsweise werden gelöschte oder aktualisierte Daten nicht automatisch historisiert, was in einigen Anwendungen problematisch sein kann. Diese Einschränkungen können durch zusätzliche Felder oder Tabellen zur Speicherung von Änderungen behoben werden.

# Migrate Funktion

![Migrate](image.png)

# Testing

Test suite starten:
`docker compose -f compose.test.yaml up --build`

# Image verkleinern

## Noch kleineres Docker-Image mit Multi-Stage Build:
```dockerfile
# STAGE 1: Build-Umgebung
FROM python:3.10.10-alpine AS builder

WORKDIR /app

# Installiere nur PIP, um das Image klein zu halten
RUN apk add --no-cache gcc musl-dev libffi-dev

# Kopiere nur die Requirements und installiere Abhängigkeiten
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt && \
    pip install --no-cache-dir --prefix=/install gunicorn

# STAGE 2: Minimales Laufzeit-Image
FROM python:3.10.10-alpine

WORKDIR /app

# Kopiere nur die benötigten Dateien aus der Build-Stage
COPY --from=builder /install /usr/local
COPY . .

# Exponiere den Port für Flask
EXPOSE 5000

# Starte den Gunicorn-Server
CMD ["gunicorn", "-b", "0.0.0.0:5000", "wsgi:app"]
```

---

## Optimierungen und Einsparungen:
1. **Multi-Stage Build:**  
   - Die Abhängigkeiten werden in einer separaten "Builder"-Stage installiert.  
   - Dadurch bleiben keine Compiler- und Build-Tools im finalen Image übrig.  

2. **Kleinste Basis (`alpine`)**:  
   - `python:3.10.10-alpine` ist viel schlanker als `slim-buster`.  

3. **Nur benötigte Systempakete (`apk add`)**:  
   - `gcc`, `musl-dev`, `libffi-dev` sind nur in der **Build-Stage** nötig, verschwinden aber im finalen Image.  

4. **`--no-cache-dir` für PIP**:  
   - Spart weiteren Speicher, da PIP keinen Cache speichert.  

5. **Kein `ADD . /app` mehr**:  
   - Stattdessen **`COPY . .`**, um unnötige Dateien zu vermeiden.  

### **Erwartete Einsparung**:
- Das Original-Image (`python:3.10.10-slim-buster`) hat **~35-40 MB**.  
- Mit `alpine` und Multi-Stage könnte das finale Image nur **10-15 MB** groß sein.  

Falls du noch mehr Platz sparen willst, kannst du in `requirements.txt` prüfen, ob unnötige Abhängigkeiten entfernt werden können.


# EC2 Instanz

IP Adress: 44.212.228.216

SSH conection: ssh -i "~/.ssh/lab-key.pem" ec2-user@34.198.175.193

