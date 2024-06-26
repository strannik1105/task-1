from fastapi import FastAPI

from src.router.router import router


def get_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router)
    return app
