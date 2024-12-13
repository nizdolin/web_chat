from fastapi import FastAPI


def create_app():
    return FastAPI(
        title="Web Chat", docs_url="/api/docs", description="A simple web chat based on Websockets, DDD and Kafka"
    )
