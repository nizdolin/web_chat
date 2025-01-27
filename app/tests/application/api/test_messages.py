import pytest
from domain.values.messages import Title
from faker import Faker
from fastapi import FastAPI
from httpx import Response
from starlette import status
from starlette.testclient import TestClient


@pytest.mark.asyncio
async def test_create_chat_success(app: FastAPI, client: TestClient, faker: Faker):
    url = app.url_path_for("create_chat_handler")
    title = faker.text(max_nb_chars=Title.MAX_LENGTH)
    response: Response = client.post(url=url, json={"title": title})

    assert response.is_success
    json_data = response.json()
    assert json_data["title"] == title


@pytest.mark.asyncio
async def test_create_chat_fail_text_too_long(app: FastAPI, client: TestClient, faker: Faker):
    url = app.url_path_for("create_chat_handler")
    title = faker.pystr(min_chars=Title.MAX_LENGTH + 1, max_chars=Title.MAX_LENGTH * 2)
    response: Response = client.post(url=url, json={"title": title})

    assert response.status_code == status.HTTP_400_BAD_REQUEST, response.json()

    json_data = response.json()
    assert json_data["detail"]["error"]


@pytest.mark.asyncio
async def test_create_chat_fail_text_empty(app: FastAPI, client: TestClient, faker: Faker):
    url = app.url_path_for("create_chat_handler")
    title = ""
    response: Response = client.post(url=url, json={"title": title})

    assert response.status_code == status.HTTP_400_BAD_REQUEST, response.json()

    json_data = response.json()
    assert json_data["detail"]["error"]
