import asyncpg
from fastapi import Depends, FastAPI
from fastapi.responses import HTMLResponse
# from datetime import datetime
#from sqlalchemy.ext.asyncio import AsyncSession
import asyncpg





from com.kimdonghee.design_pattern.creational.builder.db_builder import get_db
from com.kimdonghee.petro.web.petro_router import router as petro_router

# ✅ 싱글톤 인스턴스 가져오기
from com.kimdonghee.design_pattern.creational.singleton.db_singleton import db_singleton

# python -m uvicorn main:app --reload
app = FastAPI()


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

app.include_router(petro_router, prefix="/petro", tags=["Petro"])
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

@app.get("/users")
async def get_users(db=Depends(get_db)):
    print("😎😀➕ get/users로 진입")

    try:
        # 비동기 데이터베이스 연결 생성
        conn = await asyncpg.connect(db_singleton.db_url)
        
        query = "SELECT * FROM member"
        rows = await conn.fetch(query)
        
        result = [dict(row) for row in rows]
    
        await conn.close()
        
        return result
    except Exception as e:
        print(f"⚠️ 데이터베이스 쿼리 실행 중 오류 발생: {str(e)}")
        return {"error": str(e)}
