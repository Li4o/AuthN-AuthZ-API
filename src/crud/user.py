from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models.models import User
from src.schemas.schemas import UserCreate

async def get_user_by_email(db: AsyncSession, email: str) -> User | None:
    result = await db.execute(select(User).where(User.email == email))
    return result.scalar_one_or_none()

async def create_user(db: AsyncSession, user_in: UserCreate, hashed_password: str) -> User:
    db_user = User(
        email=user_in.email,
        hashed_password=hashed_password,
    )

    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)

    return db_user