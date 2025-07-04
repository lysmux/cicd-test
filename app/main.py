from fastapi import APIRouter, FastAPI

router = APIRouter()


@router.get("/")
async def hello() -> dict[str, str]:
    return {"message": "Hello World"}


def getapp() -> FastAPI:
    app = FastAPI()
    app.include_router(router)

    return app
