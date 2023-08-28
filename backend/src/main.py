from fastapi import FastAPI, responses
import uvicorn
import importlib
from modules import config
from modules.logger import logger


app = FastAPI()


for module in config.ROUTERS:
    logger.info(f"Registrando router '{module}'.")
    router = importlib.import_module(f"routers.{module}")
    app.include_router(
        router=router.router,
        prefix=f"/{module}",
        tags=[module.capitalize()]
    )


@app.get("/", tags=["Main"])
async def home() -> responses.RedirectResponse:
    "Página de inicio. Redirecciona a la documentación."
    logger.info("Redireccionando a la documentación.")
    return responses.RedirectResponse(app.docs_url)


@app.get("/alive", tags=["Main"])
async def alive() -> str:
    "Chequea si la aplicación está viva."
    return "Estoy vivo!"


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=8080,
        reload=True
    )
