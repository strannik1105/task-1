import uvicorn

from src import settings


def main():
    uvicorn.run("src.app:get_app", host=settings.HOST, port=settings.PORT)


if __name__ == "__main__":
    main()
