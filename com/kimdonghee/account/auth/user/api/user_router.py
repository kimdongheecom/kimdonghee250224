import os
from fastapi import APIRouter, Depends, Body, HTTPException, Request
from fastapi.responses import JSONResponse
from jose import jwt, ExpiredSignatureError, JWTError
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordBearer


from com.kimdonghee.account.auth.user.api.user_controller import UserController

from com.kimdonghee.account.auth.user.models.user_schema import UserLoginSchema, UserSchema
from com.kimdonghee.utils.creational.builder.db_builder import get_db
from com.kimdonghee.utils.config.security.redis_config import redis_client


router = APIRouter()
controller = UserController()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

SECRET_KEY = os.getenv("REFRESH_SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")


@router.get("/refresh", response_model=UserSchema)
async def refresh_token(request: Request, db: AsyncSession = Depends(get_db)):
    # 1. Authorization 헤더에서 Refresh Token 꺼내기
    auth_header = request.headers.get("Authorization")
    print("🎯 Authorization Header:", auth_header)

    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=400, detail="💥💥💥💥 Refresh token is missing or malformed")

    incoming_token = auth_header[len("Bearer "):].strip()

    try:
        # 2. JWT 디코드
        payload = jwt.decode(incoming_token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=401, detail="💥💥💥💥 Invalid token payload")
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="💥💥💥💥 Refresh token has expired")
    except JWTError:
        raise HTTPException(status_code=401, detail="💥💥💥💥 Invalid refresh token")

    # 3. Redis에서 저장된 Refresh Token과 비교
    stored_token = await redis_client.get(f"refresh_token:{user_id}")
    print("🎯🎯🎯🎯 stored_token:", stored_token)

    if stored_token != incoming_token:
        raise HTTPException(status_code=401, detail="💥💥💥💥 Invalid refresh token")
    # 4. 사용자 정보 가져와서 반환
    return None


# ✅ 로그인
@router.post("/login", response_model=UserSchema)
async def handle_login(
    user_schema: UserLoginSchema = Body(...),
    db: AsyncSession = Depends(get_db)):
    content = await controller.login(user_schema=user_schema, db=db)
    print("🔑🗝🔐🔏⛏⚒🛠content", content)
    return JSONResponse(content=content)
    



