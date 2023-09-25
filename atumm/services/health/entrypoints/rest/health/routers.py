from fastapi import Response
from fastapi.routing import APIRouter
from fastapi_restful.cbv import cbv

router = APIRouter()


@cbv(router)
class HealthRouter:
    """Health router."""

    @router.get("/health")
    async def health(self):
        return Response(status_code=200)


health_router = router
