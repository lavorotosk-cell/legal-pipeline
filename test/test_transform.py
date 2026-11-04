from legal_pipeline.transform import classifica, converti_importo

#ASSERT serve come asserzione se vera OK altrimenti mostra errore, si esegue con pytest
def test_classifica_alta():
    assert classifica(2100) == "alta"


def test_converti_importo_vuoto():
    assert converti_importo("ABC") is None