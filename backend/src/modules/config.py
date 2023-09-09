import os

APP_HOST = os.getenv("APP_HOST", "localhost")
APP_PORT = int(os.getenv("APP_PORT", "8080"))
MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_PORT = int(os.getenv("MONGO_PORT"))
MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASS = os.getenv("MONGO_PASS")
BCRA_URL = "https://www.bcra.gob.ar/SistemasFinancierosYdePagos/Sistema_financiero_nomina_de_entidades.asp?bco=AAA00&tipo=1"
ROUTERS = [
    "bank"
]
LOG_PATH = "/var/log/app.log"

APP_TITLE = "BCRA Scraper API"
APP_DESCRIPTION = "API de bancos."
APP_VERSION = "v1.0.1"
