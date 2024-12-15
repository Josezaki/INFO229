from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from ... import schemas, database
from ...crud import petitioner_evaluation_crud as crud

router = APIRouter()

def get_db():
    db = database.sessionLocal()
    try:
        yield db
    finally:
        db.close()


# Crea una evaluacion de parte del solicitante
@router.post("/petitioner_evaluation/", response_model=schemas.EvaluationPetitionerCreate)
async def create_petitioner_evaluation(
    petitioner_evaluation: schemas.EvaluationPetitionerCreate,
    db: AsyncSession = Depends(get_db)
):
    # Validamos que sea posible crear una evaluacion
    result = await crud.confirm_worker_request(db=get_db, worker_request_id=petitioner_evaluation.id_worker_request)
    if (result):
        raise HTTPException(400, "No se puede evaluar en un worker_request que no ha sido completado")
        return
    # Una vez validado, creamos el post
    result = await crud.create_petitioner_evaluation(db=get_db, petitioner_evaluation=petitioner_evaluation)
    return result

# Obtiene una evaluacion de parte del solicitante dado un id
@router.get("/petitioner_evaluation/{id_petitioner_evaluation}", response_model=schemas.EvaluationPetitioner)
async def get_petitioner_evaluation_by_id(
    id_petitioner_evaluation: int,
    db: AsyncSession = Depends(get_db)
):
    result = await crud.get_petitioner_evaluation_by_id(petitioner_id=id_petitioner_evaluation, db=get_db)
    if (result == None):
        raise HTTPException(404, "La evaluacion de parte del solicitante no existe")
    return result

# Obtiene todas las evaluaciones de un trabajador dado un id de trabajador
@router.get("/worker/{id_worker}/evaluation")
async def get_petitioner_evaluation_by_worker_id(
    id_worker: int,
    db: AsyncSession = Depends(get_db)
):
    result = await crud.get_petitioners_evaluations_by_id_worker(db=get_db, id_worker=id_worker)
    return [schemas.EvaluationPetitioner.from_orm(evaluation_petitioner) for evaluation_petitioner in result]