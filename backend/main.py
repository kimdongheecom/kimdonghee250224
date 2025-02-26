from fastapi import FastAPI

from com.kimdonghee.auth.admin.admin_router import router as admin_router
from com.kimdonghee.auth.user.user_router import router as user_router


# python -m uvicorn main:app --reload
app = FastAPI()

app.include_router(admin_router, prefix="/admin", tags=["Admin"])
app.include_router(user_router, prefix="/user", tags=["User"])

@app.get("/")
def read_root():
    return {"main": "메인 라우터"}
     # 딕셔너리 반환 #추상화: 화면(브라우저)에 글자만 준 것을 추상화라고 한다.
     # 추상화 먼저하고, 캡슐화한다. 캡슐화는 깡통만들기를 의미한다.캡슐화는 클래스를 만드는 것이다.
    