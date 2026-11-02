from sqlalchemy.ext.asyncio import create_async_engine
from src.core.config import Settings

engine = create_async_engine(
    Settings.DATABASE_URL,
    echo=True,
    future=True,
)

class Base(DeclarativeBase):
    pass

async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()