from fastapi import APIRouter
from .users_router import router as users_router
from .petitioner_router import router as petitioner_router
from .worker_router import router as worker_router
# Importa más routers aquí si es necesario.

router = APIRouter()
router.include_router(users_router, prefix="/users", tags=["User manegment"])
router.include_router(worker_router, prefix="/users", tags=["User manegment"])
router.include_router(petitioner_router, prefix="/users", tags=["User manegment"])
# Incluye más routers relacionados aquí.
