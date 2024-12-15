from fastapi import FastAPI
from . import database
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import FastAPI
#from .routers import evaluations_and_reviews
from .routers.evaluations_and_reviews import router as evaluation_and_reviews_router
from .routers.requests import router as requests_router
from .routers.services import router as services_router
from .routers.users import router as users_router

app = FastAPI()

## User router
app.include_router(users_router)

## Requests router
app.include_router(requests_router)

## Services router
app.include_router(services_router)

## evaluations and reviews router
app.include_router(evaluation_and_reviews_router)



# Event handlers
@app.on_event("startup")
async def startup():
    print("Starting up...")

@app.on_event("shutdown")
async def shutdown():
    print("Shutting down...")


# app = FastAPI()

# # Configuración de los routers 

# app.include_router(users_router.router)
# app.include_router(petitioner_router.router)
# app.include_router(worker_router.router)
# app.include_router(request_router.router)
# app.include_router(worker_request_router.router)
# app.include_router(worker_review_router.router)
# app.include_router(petitioner_review_router.router)
# app.include_router(services_router.router)
# app.include_router(petitioner_service_router.router)
# app.include_router(petitioner_evaluation_router.router)
# app.include_router(worker_evaluation_router.router)


# # Event handlers para manejar el ciclo de vida de la app
# @app.on_event("startup")
# async def startup():
#     pass

# @app.on_event("shutdown")
# async def shutdown():
#     pass

