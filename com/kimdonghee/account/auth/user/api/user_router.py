from fastapi import APIRouter, Depends, Body, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordBearer

from com.kimdonghee.account.auth.user.api.user_controller import UserController
from com.kimdonghee.account.auth.user.models.user_schema import UserLoginSchema
from com.kimdonghee.utils.creational.builder.db_builder import get_db


router = APIRouter()
controller = UserController()

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


# ✅ 로그인
@router.post("/login")
async def handle_login(
    login_data: UserLoginSchema = Body(...),
    db: AsyncSession = Depends(get_db)
):
    print("🎋🎄🎍", "router에서 handle_login으로 진입함")
    return await controller.login(login_data=login_data, db=db)




