import csv
from pathlib import Path
import json

def leggi_ordini(percorso: Path) -> list[dict]:
    with open(percorso, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def scrivi_json(dati: list[dict], percorso: Path) -> None:
    percorso.parent.mkdir(parents=True, exist_ok=True) # crea le cartelle se mancano
    with open(percorso, "w", encoding="utf-8") as f:
        # ensure_ascii=False mantiene le lettere accentate leggibili e indent=2 rende il file ordinato.
        json.dump(dati, f, ensure_ascii=False, indent=2) 