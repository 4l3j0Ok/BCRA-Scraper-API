import requests
from . import config
from .logger import logger


def get_latest_image_version():
    try:
        response = requests.get(config.DOCKER_API_URL)
        logger.error(config.DOCKER_API_URL)
        logger.error(response)
        data = response.json()
        for result in data["results"]:
            if result["name"] != "latest":
                return result["name"]
    except Exception as ex:
        logger.error("Hubo un error al obtener la última versión de la imagen de Docker.")
        logger.exception(ex)
    return "latest"