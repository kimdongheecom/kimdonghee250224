
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from contextlib import asynccontextmanager

from com.kimdonghee.app_router import router as app_router

from fastapi.middleware.cors import CORSMiddleware

from com.kimdonghee.utils.creational.builder.db_builder import engine


load_dotenv()
# python -m uvicorn main:app --reload
app = FastAPI()

# ✅ CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인 허용 (실제 배포 시 보안 고려 필요)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ 애플리케이션 시작 시 `init_db()` 실행
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀🚀🚀🚀 FastAPI 앱이 시작됩니다. 데이터베이스 초기화 중...")
    # await init_db()  # ✅ DB 초기화 실행
    # print("✅ 데이터베이스 초기화 완료!")
    yield  # 애플리케이션이 실행되는 동안 유지
    print("🛑 FastAPI 앱이 종료됩니다.")
    await engine.dispose()  # 🔥 모든 커넥션 정리
    print("✅ DB 연결이 정상적으로 종료되었습니다.")

# ✅ 라우터 등록
app.include_router(app_router,prefix="/api") #aap은 메인라우터이다.
print("😎😀➕ 메인 라우터로 진입")

def current_time():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ✅ 싱글톤 인스턴스 생성
# db_config = db_singleton

# ✅ PostgreSQL 비동기 연결 함수
# async def connect_db():
#     return await asyncpg.connect(DATABASE_URL)

# app.include_router(petro_router, prefix="/petro", tags=["Petro"])
# current_time: Callable[[], str] = lambda: datetime.now(datetime.timezone('Asia/Seoul')).strftime("%Y-%m-%d %H:%M:%S")

@app.get(path="/")
async def home():
    return HTMLResponse(content=f"""
<body>
<div style="width: 400px; margin: 50 auto;">
    <h1> 현재 서버 구동 중입니다.</h1>

</div>
</body>
""")

