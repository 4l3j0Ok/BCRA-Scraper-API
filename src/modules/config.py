import os


APP_HOST = os.getenv("APP_HOST", "localhost")
APP_PORT = int(os.getenv("APP_PORT", "8080"))
MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    MONGO_HOST = os.getenv("MONGO_HOST")
    MONGO_PORT = int(os.getenv("MONGO_PORT"))
    MONGO_USER = os.getenv("MONGO_USER")
    MONGO_PASS = os.getenv("MONGO_PASS")
BCRA_URL = "https://www.bcra.gob.ar/SistemasFinancierosYdePagos/Sistema_financiero_nomina_de_entidades.asp?bco=AAA00&tipo=1"
DOCKER_ORGANIZATION = os.getenv("DOCKER_ORGANIZATION", "alejoide")
DOCKER_REPOSITORY = os.getenv("DOCKER_REPOSITORY", "bcra-scraper-api")
DOCKER_API_URL = f"https://registry.hub.docker.com/v2/repositories/{
    DOCKER_ORGANIZATION}/{DOCKER_REPOSITORY}/tags"
ROUTERS = [
    "bank"
]
LOG_PATH = "/var/log/app.log"

APP_TITLE = "BCRA Scraper API"
APP_DESCRIPTION = "API de bancos."
