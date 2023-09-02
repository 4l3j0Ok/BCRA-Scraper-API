# BCRA Scraper API

<div align=center>

![Logo](./resources/repo-logo.png)

[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)![Static Badge](https://img.shields.io/badge/3.11-blue?style=for-the-badge)](https://www.python.org/downloads/release/python-3114/) [![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)![Static Badge](https://img.shields.io/badge/6.0-white?style=for-the-badge)](https://www.mongodb.com/docs/manual/release-notes/6.0/)
 [![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com/) [![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/cb7bca4e391f4b1a953f233796628bab)](https://app.codacy.com/gh/4l3j0Ok/BCRA-Scraper-API/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade) [![Docker Image Version (latest semver)](https://img.shields.io/docker/v/alejoide/bcra-scraper-api)](https://hub.docker.com/r/alejoide/bcra-scraper-api) [![Docker Image Size (tag)](https://img.shields.io/docker/image-size/alejoide/bcra-scraper-api/1.0.0)](https://hub.docker.com/r/alejoide/bcra-scraper-api) 

</div>

## Introducción

API creada con FastAPI que utiliza scraping para obtener la lista de bancos oficiales publicados por BCRA.

Mediante la API se podrá administrar la lista de bancos obtenidos y guardados en la base de datos.

Además, al estar crada con FastAPI, la documentación de la API está creada automáticamente y se puede acceder mediante el path `/docs` (Swagger UI) o `/redoc` (ReDoc).
