from flask import jsonify, request
from apiflask.fields import Float
from apiflask import APIFlask, Schema
import requests

app = APIFlask(__name__, docs_path='/docs')

# Schema für die Eingabeparameter (Query-Parameter a und b)
class CalcInput(Schema):
    a = Float(required=True, example=5.0)
    b = Float(required=True, example=2.0)

# Schema für die Ausgabe (das Ergebnis)
class CalcOutput(Schema):
    result = Float()

class ConvertInput(Schema):
    amount = Float(required=True, example=100.0)
 
class ConvertOutput(Schema):
    btc_amount = Float()

@app.route('/')
def hello_world():
    return 'Hello ITCNE24!'

@app.get("/calc/<op>")
@app.input(CalcInput, location="query")  # Validiert die Query-Parameter a und b
@app.output(CalcOutput)
def calculater(op):
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)

    if a is None or b is None or op is None:
        return jsonify({"error": "Invalid parameters"}), 400

    if op == "add":
        result = a + b
    elif op == "sub":
        result = a - b
    elif op == "mul":
        result = a * b          
    elif op == "div":
        if b == 0:
            return jsonify({"error": "Division by zero"}), 400
        result = a / b
    else:
        return jsonify({"error": "Invalid operation"}), 400

    return jsonify({"result": result})

@app.route('/convert', methods=['GET'])
@app.input(ConvertInput, location="query")  
@app.output(ConvertOutput)
def convert_to_btc(query_data):
    try:
        amount_eur = float(query_data.get('amount', 0))
        if amount_eur <= 0:
            return jsonify({"error": "Invalid amount"}), 400

        # Abrufen des aktuellen BTC-USD-Kurses
        response = requests.get("https://data-api.coindesk.com/index/cc/v1/latest/tick?market=cadli&instruments=BTC-USD")
        api_data = response.json()  # JSON-Daten abrufen
        
        print(api_data)  # Debugging: API-Antwort in der Konsole ausgeben

        # Überprüfen, ob die erwartete Struktur vorhanden ist
        if "Data" not in api_data or "BTC-USD" not in api_data["Data"] or "VALUE" not in api_data["Data"]["BTC-USD"]:
            return jsonify({"error": "Unexpected API response", "response": api_data}), 500

        btc_usd = api_data["Data"]["BTC-USD"]["VALUE"]  # Neuer Zugriffspfad!

        # Umrechnung von EUR nach USD (angenommener Kurs, könnte durch API ersetzt werden)
        eur_usd = 1.1  # Beispielkurs
        amount_usd = amount_eur * eur_usd

        # Umrechnung in BTC
        btc_amount = amount_usd / btc_usd

        return jsonify({"amount_eur": amount_eur, "amount_btc": btc_amount})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

