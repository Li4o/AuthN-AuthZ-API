from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from src.core.config import Settings

# 設定クラスのインスタンス作成
settings = Settings()
# データベースURLの取得
DATABASE_URL = settings.DATABASE_URL.get_secret_value()

# データベース接続設定
engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    future=True,
)

# 非同期セッション設定
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# データベーステーブルクラスの宣言
class Base(DeclarativeBase):
    pass

# データベース取得処理
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