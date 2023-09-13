from atumm.extensions.buti.keys import AtummContainerKeys
from atumm.services.health.entrypoints.rest.health.routers import health_router
from buti import BootableComponent, ButiStore
from fastapi import FastAPI


class HealthServiceComponent(BootableComponent):
    def boot(self, object_store: ButiStore):
        app: FastAPI = object_store.get(AtummContainerKeys.app)
        app.include_router(health_router)
