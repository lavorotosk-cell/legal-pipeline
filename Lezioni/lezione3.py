import csv
from pathlib import Path
import json

def classifica(importo: float) -> str:
    if   importo > 2000: 
        return "alta"
    elif importo > 1000: 
        return "media"
    else: 
        return "bassa"

def leggi_ordini(percorso: Path) -> list[dict]:
    with open(percorso, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def converti_importo(valore: str) -> float | None:
    try:
        return float(valore)
    except ValueError:
        return None

def elabora_ordini(ordini: list[dict]) -> tuple[list[dict], list[dict]]:
    ordini_validi: list[dict] = []
    ordini_scartati: list[dict] = []

    for ordine in ordini:
        try:
            importo = converti_importo(ordine["importo"])
            if importo is None:
                ordini_scartati.append(ordine)
                continue
            ordine["importo"] = importo 
            ordine["fascia"] = classifica(importo)
            ordini_validi.append(ordine)
        except KeyError:
            ordini_scartati.append(ordine)


    return ordini_validi,ordini_scartati

def scrivi_json(dati: list[dict], percorso: Path) -> None:
    percorso.parent.mkdir(parents=True, exist_ok=True) # crea le cartelle se mancano
    with open(percorso, "w", encoding="utf-8") as f:
        # ensure_ascii=False mantiene le lettere accentate leggibili e indent=2 rende il file ordinato.
        json.dump(dati, f, ensure_ascii=False, indent=2) 

    
ordini = leggi_ordini(Path("samples") / "ordini.csv")
validi, scartati = elabora_ordini(ordini)
clienti_alta = [c["cliente"] for c in validi if c["fascia"] == "alta"]

print(f"righe lette: {len(ordini)}")
print(ordini[0])

print(f"{converti_importo('1250.50')}")
print(f"{converti_importo('')}")
print(f"{converti_importo('abc')}")

print(f"Numero ordini validi: {len(validi)}")
print(f"Numero ordini scartati: {len(scartati)}")
print(f"Totale importi validi: {sum(o['importo'] for o in validi):.2f}")

print(f"{clienti_alta}")

scrivi_json(validi, Path("data") / Path("output") / "validi.json")
scrivi_json(scartati, Path("data") / Path("output") / "scartati.json")
