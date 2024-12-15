from fastapi import APIRouter
from .petitioner_evaluation_router import router as petitioner_evaluation_router
from .petitioner_review_router import router as petitioner_review_router
from .worker_evaluation_router import router as worker_evaluation_router
from .worker_review_router import router as worker_review_router

# Importa más routers aquí si es necesario.

router = APIRouter()
router.include_router(petitioner_evaluation_router, prefix="/evaluation-and-requests", tags=["Evaluations and Requests management"])
router.include_router(petitioner_review_router, prefix="/evaluation-and-requests", tags=["Evaluations and Requests management"])
router.include_router(worker_evaluation_router, prefix="/evaluation-and-requests", tags=["Evaluations and Requests management"])
router.include_router(worker_review_router, prefix="/evaluation-and-requests", tags=["Evaluations and Requests management"])
# Incluye más routers relacionados aquí.


