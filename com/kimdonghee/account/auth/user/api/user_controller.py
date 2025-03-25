from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from com.kimdonghee.account.auth.user.models.user_entity import UserEntity
from com.kimdonghee.account.auth.user.models.user_schema import UserSchema, UserLoginSchema



class UserController:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    # ✅ 로그인
    async def login(self, login_data: UserLoginSchema, db: AsyncSession):
        result = await db.execute(select(UserEntity).where(UserEntity.user_id == login_data.user_id))
        user = result.scalar()
        if not user or not self.pwd_context.verify(login_data.password, user.password):
            return None


    # ✅ 현재 사용자 조회 (JWT 토큰 검증 필요 시 확장)
    async def get_current_user(self, token: str):
        # 향후: JWT 디코딩 및 사용자 조회 구현 예정
        return token  # 임시 구현


