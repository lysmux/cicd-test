from os import getenv

from fastapi import APIRouter, FastAPI

router = APIRouter()


@router.get("/")
async def hello() -> dict[str, str]:
    return {"message": "Hello World"}

@router.get("/env")
async def env() -> dict[str, str]:
    return {"env": getenv("ENVIRONMENT", "Undefined")}

def getapp() -> FastAPI:
    app = FastAPI()
    app.include_router(router)

    return app
