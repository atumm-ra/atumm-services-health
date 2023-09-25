import pytest
from httpx import AsyncClient
from starlette.responses import Response


@pytest.mark.anyio
async def test_health(client: AsyncClient):
    response: Response = await client.get("/health")
    assert response.status_code == 200
