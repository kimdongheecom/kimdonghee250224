
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from com.kimdonghee.app_router import router as app_router

# python -m uvicorn main:app --reload
app = FastAPI()

app.include_router(app_router) #aap은 메인라우터이다.
print("😎😀➕ 메인 라우터로 진입")


# ✅ 싱글톤 인스턴스 생성
# db_config = db_singleton
# print("🎋🎄🎍",db_config.db_hostname)
# print("🎋🎄🎍",db_config.db_username)
# print("🎋🎄🎍",db_config.db_password)
# print("🎋🎄🎍",db_config.db_port)
# print("🎋🎄🎍",db_config.db_database)
# print("🎋🎄🎍",db_config.db_charset)


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

