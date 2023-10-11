import requests
import json

# Funzione per ottenere gli snapshot di un URL per un anno specifico
def get_snapshots_for_year(url, year):
    wayback_api_url = f"http://archive.org/wayback/available?url={url}&timestamp={year}0101000000"
    response = requests.get(wayback_api_url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

# Chiedi all'utente l'URL da cercare nella Wayback Machine
url_to_check = input("URL: ")

# Chiedi all'utente l'anno di inizio e fine
start_year = int(input("start date: "))
end_year = int(input("end date: "))

# Esegui le richieste per ogni anno e stampa i risultati
results = []
for year in range(start_year, end_year + 1):
    snapshot_data = get_snapshots_for_year(url_to_check, year)
    if snapshot_data:
        results.append(snapshot_data)

# Stampa i risultati in formato JSON
if results:
    print(json.dumps(results, indent=4))
else:
    print(f"No result found {start_year}-{end_year} for this url.")
