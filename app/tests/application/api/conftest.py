import pytest
from application.api.main import create_app
from fastapi import FastAPI
from logic.init import init_container
from starlette.testclient import TestClient
from tests.fixtures import init_dummy_container


@pytest.fixture
def app() -> FastAPI:
    application = create_app()
    application.dependency_overrides[init_container] = init_dummy_container

    return application


@pytest.fixture
def client(app: FastAPI) -> TestClient:
    return TestClient(app)
