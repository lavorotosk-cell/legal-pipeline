import logging
from pathlib import Path

from legal_pipeline.files import leggi_ordini, scrivi_json
#from legal_pipeline.transform import elabora_ordini

logger = logging.getLogger(__name__)


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    ordini = leggi_ordini(Path("samples") / "ordini.csv")
    logger.info("righe lette: %s", len(ordini))
    # ... da completare


if __name__ == "__main__":
    main()