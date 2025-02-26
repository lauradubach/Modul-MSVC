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
```

Dieses Markdown-Format kann direkt in einem Markdown-Editor oder GitHub verwendet werden. 🎯