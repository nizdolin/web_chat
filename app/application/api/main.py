from fastapi import FastAPI


def create_app():
    return FastAPI(title='Web Chat', docs_url='/api/docs', description="Simple Websocket chat based on DDD and Kafka")
