from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException
from .. import models, schemas
from typing import Optional, List

# Obtiene todos los usuarios con filtros opcionales

async def get_users(
    db: AsyncSession,
    first_name_starts_with: Optional[str] = None,
    lastname_starts_with: Optional[str] = None,
    age_greater_than: Optional[int] = None
) -> List[models.User]:
    query = select(models.User)
    
    if first_name_starts_with:
        query = query.filter(models.User.first_name.like(f"{first_name_starts_with}%"))
    
    if lastname_starts_with:
        query = query.filter(models.User.lastname.like(f"{lastname_starts_with}%"))
    
    if age_greater_than:
        query = query.filter(models.User.age > age_greater_than)

    try:
        result = await db.execute(query)
        users = result.scalars().all()
        
        if not users:
            raise HTTPException(status_code=404, detail="No users found matching the criteria")
        
        return users
    
    except Exception as e:
        # Captura errores generales con detalles adicionales
        raise HTTPException(status_code=500, detail=f"Error occurred while fetching users: {str(e)}")


# Obtiene un usuario por id
async def get_user_by_id(db: AsyncSession, user_id: int):
    result = await db.execute(select(models.User).filter(models.User.id == user_id))
    user = result.scalars().first()
    return user

#Crear usuario
async def create_user(db: AsyncSession, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

 #Visualizar perfiles de usuario
async def visualize_user_profile (db: AsyncSession, user_id: int):
    result = await db.execute(select(models.User).filter(models.User.id == user_id))
    return result.scalars().first()

# Editar perfil 
async def edit_profile (db: AsyncSession, user_id: int, user: schemas.UserBase):
    result = await db.execute(select(models.User).filter(models.User.id == user_id))
    user_db = result.scalars().first()
    user_db.lastname = user.lastname
    user_db.phone_number = user.phone_number

# Cambiar contraseña
async def change_password (db: AsyncSession, user_id: int, user: schemas.UserLogin):
    result = await db.execute(select(models.UserLogin).filter(models.UserLogin.id_user == user_id))
    user_db = result.scalars().first()
    user_db.pass_hash = user.pass_hash

# Create user login
async def create_user_login(db: AsyncSession, user_login: schemas.UserLoginCreate):
    
    # Verificamos si el ID existe
    db_user_login = await db.execute(select(models.User).filter(models.User.id == user_login.id_user))
    db_user_login = db_user_login.scalars().first()
    if db_user_login == None:
        raise HTTPException(status_code=404, detail="The user ID does not exists")
    
    # Verificamos que el mail no exista
    db_user_login = await db.execute(select(models.UserLogin).filter(models.UserLogin.mail == user_login.mail))
    db_user_login = db_user_login.scalars().first()
    if db_user_login != None:
        raise HTTPException(status_code=404, detail="The mail already exists")

    db_user_login = models.UserLogin(**user_login.dict())
    db.add(db_user_login)
    await db.commit()
    await db.refresh(db_user_login)
    return db_user_login

# Verificar login
async def get_user_login(db: AsyncSession, mail: str):
    result = await db.execute(select(models.UserLogin).filter(models.UserLogin.mail == mail))
    user_login = result.scalars().first()
    return user_login


# Verifica si un RUT o número de teléfono ya está en uso
async def check_rut_or_phone_in_use(db: AsyncSession, phone: int, rut: int):
    # Verificar el número de teléfono
    phone_exists = await db.execute(select(models.User).filter(models.User.phone_number == phone))
    phone_exists = phone_exists.scalars().first()

    if phone_exists:
        raise HTTPException(status_code=400, detail="Phone number is already in use")

    # Verificar el RUT
    rut_exists = await db.execute(select(models.User).filter(models.User.rut == rut))
    rut_exists = rut_exists.scalars().first()

    if rut_exists:
        raise HTTPException(status_code=400, detail="RUT is already in use")

    return None

# Obtener login por ID de usuario
async def get_user_login_by_id(db: AsyncSession, user_id: int):
    result = await db.execute(select(models.UserLogin).filter(models.UserLogin.id_user == user_id))
    user_login = result.scalars().first()
    return user_login

