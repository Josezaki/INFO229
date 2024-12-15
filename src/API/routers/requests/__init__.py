from fastapi import APIRouter
from .requests_router import router as requests_router
from .worker_request_router import router as worker_request_router
# Importa más routers aquí si es necesario.

router = APIRouter()
router.include_router(requests_router, prefix="/requests", tags=["Request manegment"])
router.include_router(worker_request_router, prefix="/requests", tags=["Request manegment"])

# Incluye más routers relacionados aquí.


