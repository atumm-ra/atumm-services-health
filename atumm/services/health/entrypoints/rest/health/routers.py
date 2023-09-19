from atumm.extensions.fastapi.routable import Routable, bind_router
from fastapi import Response
from fastapi.routing import APIRouter

router = APIRouter()


@bind_router(router)
class HealthRouter(Routable):
    """Home router."""

    @router.get("/health")
    async def health(self):
        return Response(status_code=200)


health_router = HealthRouter().router
