from fastapi import APIRouter
from .services_router import router as services_router
from .petitioner_service_router import router as petitioner_service_router
# Importa más routers aquí si es necesario.

router = APIRouter()
router.include_router(services_router, prefix="/services", tags=["Service manegment"])
router.include_router(petitioner_service_router, prefix="/services", tags=["Service manegment"])
# Incluye más routers relacionados aquí.


