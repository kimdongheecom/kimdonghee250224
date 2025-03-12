from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import os

load_dotenv()  # ✅ .env 강제 로드

DATABASE_URL = os.getenv("DB_URL")  # ✅ .env에서 직접 가져옴

if not DATABASE_URL:
    raise ValueError("❌ DATABASE_URL이 설정되지 않았습니다. .env 파일을 확인하세요.")

engine = create_async_engine(DATABASE_URL, echo=True)

# ✅ 비동기 세션 팩토리 생성
SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,  # 비동기 세션 사용
    expire_on_commit=False
)

Base = declarative_base()

# ✅ 비동기 세션 가져오는 함수
async def get_db():
    async with SessionLocal() as session:
        yield session