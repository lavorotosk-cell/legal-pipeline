from legal_pipeline.transform import elabora_ordini

# Un problema di struttura nello stesso file.
# elabora_ordini(ordini) viene eseguita a livello di modulo,
# cioè durante la raccolta dei test, non dentro un test.
# Se la funzione sollevasse un errore, pytest fallirebbe prima ancora di eseguire i test.
# Spostala dentro una funzione di supporto o in ogni test


def crea_ordini() -> list[dict]:
    return [
        {"id": "1", "importo": "123"},
        {"id": "2", "importo": ""},
        {"id": "3", "importo": "abc"},
    ]


# validi, scartati = elabora_ordini(ordini)


def test_num_ordini_validi():
    validi, _ = elabora_ordini(crea_ordini())
    assert len(validi) == 1


def test_num_ordini_scartati():
    _, scartati = elabora_ordini(crea_ordini())
    assert len(scartati) == 2


def test_importo():
    validi, _ = elabora_ordini(crea_ordini())
    assert validi[0]["importo"] == 123.0
