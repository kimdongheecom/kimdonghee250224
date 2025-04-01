from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from com.kimdonghee.account.auth.user.api.user_factory import UserFactory
from com.kimdonghee.account.auth.user.models.user_action import UserAction
from com.kimdonghee.account.auth.user.models.user_entity import UserEntity
from com.kimdonghee.account.auth.user.models.user_schema import UserSchema, UserLoginSchema



class UserController:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    # ✅ 로그인
    async def login(self, **kwargs):
        print("🎋🎄🎍컨트롤러로 진입,kwargs", **kwargs)
    async def create_new_user(self, **kwargs):
        return await UserFactory.create(UserAction.CREATE_NEW_USER, **kwargs)
    
    async def login(self, **kwargs):
        return await UserFactory.create(UserAction.LOGIN, **kwargs)
    
    async def logout(self, **kwargs):
        return await UserFactory.create(UserAction.LOGOUT, **kwargs)


