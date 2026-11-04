ordini: list[dict] = [
    {"id": 1, "cliente": "Rossi", "importo": 1250.50},
    {"id": 2, "cliente": "Bianchi", "importo": 980.00},
    {"id": 3, "cliente": "Verdi", "importo": None},
    {"id": 4, "cliente": "Neri", "importo": 2100.00},
]

ordini.append({"id": 5, "cliente": "Gialli"})

importi: list[float] = [1250.50, 980.00, 1750.25, 430.75, 2100.00]


def classifica(importo: float) -> str:
    if importo > 2000:
        return "alta"
    elif importo > 1000:
        return "media"
    else:
        return "bassa"


print(f"l'importo 5000 è {classifica(importo=5000)}")
print(f"l'importo 1 è {classifica(importo=1)}")
print(f"l'importo 1111 è {classifica(importo=1111)}")

for pos, importo in enumerate(importi, start=1):
    print(f"importo {pos}: {importo:.2f} -> {classifica(importo)}")


def elabora(ordini: list[dict]) -> tuple[list[dict], list[dict]]:
    ordini_validi: list[dict] = []
    ordini_scartati: list[dict] = []

    for ordine in ordini:
        try:
            importo = ordine["importo"]
        except KeyError:
            ordini_scartati.append(ordine)
            continue

        if importo is None:
            ordini_scartati.append(ordine)
            continue
        # TRY e IF si possono sostituire con IF ordine.get("importo") is None
        ordine["fascia"] = classifica(importo)
        ordini_validi.append(ordine)

    return ordini_validi, ordini_scartati


validi, scartati = elabora(ordini)

print(f"Numero ordini validi: {len(validi)}")
print(f"Numero ordini scartati: {len(scartati)}")
print(f"Totale importi validi: {sum(o['importo'] for o in validi):.2f}")
