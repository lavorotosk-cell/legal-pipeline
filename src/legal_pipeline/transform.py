def classifica(importo: float) -> str:
    if importo > 2000:
        return "alta"
    elif importo > 1000:
        return "media"
    else:
        return "bassa"


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
    return ordini_validi, ordini_scartati
