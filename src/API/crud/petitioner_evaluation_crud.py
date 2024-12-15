from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from .. import models, models, database

# Confirma si el worker_request esta resuelto
async def confirm_worker_request(
    db: AsyncSession,
    worker_request_id: int
) -> bool:
    query = (
        select(models.WorkerRequest).
        where(models.WorkerRequest.worker_request_id == worker_request_id and models.WorkerRequest.solved == True)
    )
    result = await db.execute(query)
    return not (result == None)

# Crear un nuevo registro de petitioner_evaluation
async def create_petitioner_evaluation(
    db: AsyncSession,
    petitioner_evaluation: models.EvaluationPetitioner
):
    db_petitioner_evaluation = models.EvaluationPetitioner(**petitioner_evaluation.dict())
    db.add(db_petitioner_evaluation)
    await db.commit()
    await db.refresh(db_petitioner_evaluation)
    return db_petitioner_evaluation

# Obtener un registro de petitioner_evaluation por id
async def get_petitioner_evaluation_by_id(
    db: AsyncSession,
    petitioner_id: int
):
    result = await db.execute(select(models.EvaluationPetitioner).filter(models.EvaluationPetitioner.id == petitioner_id))
    return result.scalars().first()

# Obtener todos los registros de petitioner_evaluation dado un id_service
async def get_petitioners_evaluations_by_id_worker(
    db: AsyncSession,
    worker_id: int
) -> List[models.EvaluationPetitioner]:
    query = (
        select(models.EvaluationPetitioner).
        join(models.WorkerRequest, models.EvaluationPetitioner.id_worker_request == models.WorkerRequest.id).
        join(models.Worker, models.Worker.id == models.WorkerRequest.id_worker).
        where(models.Worker.id == worker_id)
    )
    result = await db.execute(query)
    return result.scalars().all()