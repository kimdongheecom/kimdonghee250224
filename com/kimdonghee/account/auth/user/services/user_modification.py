from sqlalchemy.ext.asyncio import AsyncSession
from com.kimdonghee.account.auth.user.models.user_entity import UserEntity
from com.kimdonghee.account.auth.user.models.user_schema import UserSchema
from com.kimdonghee.utils.creational.abstract.abstract_service import AbstractService


class UserModification(AbstractService):
    async def handle(self, **kwargs):
        try:
            return "success"
        except Exception as e:
            return "fail"


class UserDeletion(AbstractService):
    async def handle(self, **kwargs):
        try:
            return "success"
        except Exception as e:
            return "fail"


