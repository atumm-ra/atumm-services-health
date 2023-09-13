import os
from typing import AsyncIterator

import httpx
import pytest
from atumm.core.infra.config import Config
from atumm.extensions.fastapi.base import TestWebApp
from atumm.services.health.entrypoints.rest.health.routers import health_router
from fastapi.applications import FastAPI


@pytest.fixture
def anyio_backend():
    return "asyncio"


class AppConfig(Config):
    STAGE: str = "test"
    DEBUG: bool = True

    API_TITLE: str = "My API"
    API_DESCRIPTION: str = ""
    API_VERSION: str = "1.0.0"


@pytest.fixture
async def client() -> AsyncIterator[httpx.AsyncClient]:
    app: FastAPI = TestWebApp(AppConfig()).app
    app.include_router(health_router)
    async with httpx.AsyncClient(app=app, base_url="http://testhost") as client:
        yield client
