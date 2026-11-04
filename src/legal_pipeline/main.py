import logging
from pathlib import Path

from legal_pipeline.files import leggi_ordini, scrivi_json
from legal_pipeline.transform import elabora_ordini

logger = logging.getLogger(__name__)


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    ordini = leggi_ordini(Path("samples") / "ordini.csv")
    logger.info("righe lette: %s", len(ordini))
    validi, scartati = elabora_ordini(ordini)
    logger.info("ordini validi: %s", len(validi))
    logger.warning("ordini scartati: %s", len(scartati))
    scrivi_json(validi, Path("data")  /Path("output") / "validi.json" )
    logger.info("gli ordini validi hanno un importo totale di %s euro", sum(v['importo'] for v in validi))
    scrivi_json(scartati, Path("data")  /Path("output") / "scartati.json" )
    


if __name__ == "__main__":
    main()