from legal_pipeline.transform import classifica, converti_importo

#ASSERT serve come asserzione se vera OK altrimenti mostra errore, si esegue con pytest
def test_classifica_alta():
    assert classifica(2100) == "alta"

def test_classifica_media():
    assert classifica(1500) == "media"

def test_classifica_media_confine():
    assert classifica(2000) == "media"

def test_converti_importo_corretto():
    assert converti_importo("1250.50") == 1250.50

def test_converti_importo_errato():
    assert converti_importo("abc") is None
