from fastapi import APIRouter, FastAPI

router = APIRouter()

@router.get("/")
async def hello():
    return {"message": "Hello World"}


def getapp() -> FastAPI:
    app = FastAPI()
    app.include_router(router)

    return app
