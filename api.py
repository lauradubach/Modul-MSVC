import requests
import json

# Lade die Konfigurationsdatei
with open('./config.json', 'r') as f:
    config = json.load(f)

API_KEY = config["TICKETMASTER_API_KEY"]
url = "https://app.ticketmaster.com/discovery/v2/events.json"
params = {
    "apikey": API_KEY,
    "countryCode": "DE",  # Zum Beispiel für Deutschland
    "classificationName": "music"  # Du kannst nach Kategorie wie Musik filtern
}

def fetch_and_structure_events():
    response = requests.get(url, params=params)

    if response.status_code == 200:
        events = response.json().get("_embedded", {}).get("events", [])
        structured_events = []

        for event in events:
            event_data = {
                "title": event.get("name", "No title available"),
                "start": event.get("dates", {}).get("start", {}).get("localDate", "No date available"),
                "end": event.get("dates", {}).get("end", {}).get("localDate", "No end date available"),
                "location": event.get("_embedded", {}).get("venues", [{}])[0].get("name", "No venue available"),
                "city": event.get("_embedded", {}).get("venues", [{}])[0].get("city", {}).get("name", "No city available"),
                "country": event.get("_embedded", {}).get("venues", [{}])[0].get("country", {}).get("name", "No country available"),
                "url": event.get("url", "No URL available")
            }

            # Füge den Künstlernamen hinzu, falls vorhanden
            if "attractions" in event:
                artists = [artist.get("name") for artist in event["attractions"]]
                event_data["artists"] = ", ".join(artists) if artists else "No artist available"

            structured_events.append(event_data)

        # Ausgabe der strukturierten Events
        print(json.dumps(structured_events, indent=4, ensure_ascii=False))
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    fetch_and_structure_events()