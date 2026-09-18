import requests

url = 'http://127.0.0.1:8000/indicators'
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

# Lista de datos diferentes para cada petición
indicadores = [
    {
        "type": "ip",
        "value": "8.8.8.8",
        "source": "feed1",
        "confidence": 50,
        "threat_type": "malware",
        "tags": ["botnet"]
    },
    {
        "type": "ip",
        "value": "999.999.999.999",
        "source": "feed2",
        "confidence": 50,
        "threat_type": "phishing",
        "tags": ["phishing", "2024"]
    },
    {
        "type": "domain",
        "value": "google.com",
        "source": "feed2",
        "confidence": 80,
        "threat_type": "phishing",
        "tags": ["phishing", "2024"]
    },
    {
        "type": "domain",
        "value": "esto_no_es_un_dominio",
        "source": "feed2",
        "confidence": 80,
        "threat_type": "phishing",
        "tags": ["phishing", "2024"]
    },
    {
        "type": "hash",
        "value": "esto_no_es_un_dominio",
        "source": "feed2",
        "confidence": 100,
        "threat_type": "phishing",
        "tags": ["phishing", "2024"]
    },
    {
        "type": "ip",
        "value": "8.8.8.8",
        "source": "feed2",
        "confidence": 150,
        "threat_type": "phishing",
        "tags": ["phishing", "2024"]
    },
    # ... más registros
]

for indicador in indicadores:
    resultado = requests.post(url, json=indicador, headers=headers)
    print(f"Status: {resultado.status_code} - {indicador['value']}")
    if resultado.status_code != 200 and resultado.status_code != 201:
        print(f"  Error: {resultado.text}")