from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from .. import models, schemas, database

# Crear un nuevo registro de petitioner_review
async def create_petitioner_review(
    db: AsyncSession,
    petitioner_review: schemas.PetitionerReviewCreate
):
    db_petitioner_review = models.PetitionerReview(**petitioner_review.dict())
    db.add(db_petitioner_review)
    await db.commit()
    await db.refresh(db_petitioner_review)
    return db_petitioner_review

# Obtener un registro de petitioner_review por id
async def get_petitioner_review_by_id(
    db: AsyncSession,
    petitioner_review_id: int
):
    result = await db.execute(select(models.PetitionerReview).filter(models.PetitionerReview.id == petitioner_review_id))
    return result.scalars().first()

# Obtener todos los registros de petitioner_review dada un id_service
async def get_petitioners_reviews_by_id_service(
    db: AsyncSession,
    service_id: int
) -> List[models.PetitionerReview]:
    query=(
        select(models.PetitionerReview).
        join(models.PetitionerService, models.PetitionerService.id == models.PetitionerReview.id_petitioner_service).
        where(models.PetitionerService.id == service_id)
    )

    result = await db.execute(query)
    return result.scalars().all()