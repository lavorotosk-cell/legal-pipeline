from legal_pipeline.transform import elabora_ordini

ordini: list[dict] = [
    { "id" : 1,  "importo" : "123"},
    { "id" : 1,  "importo" : ""},
    { "id" : 1,  "importo" : "abc"},
    ]

validi, scartati = elabora_ordini(ordini)

def test_num_ordini_validi():
    assert len(validi) == 1

def test_num_ordini_scartati():
    assert len(scartati) == 2

def test_importo():
    assert float(validi[0]["importo"]) is True

