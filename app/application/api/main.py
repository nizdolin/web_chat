from application.api.messages.handlers import router
from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(
        title="Web Chat",
        docs_url="/api/docs",
        description="A simple web chat based on Websockets, DDD and Kafka",
        debug=True,
    )
    app.include_router(router, prefix="/chat")

    return app
