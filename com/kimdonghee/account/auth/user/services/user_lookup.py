
from com.kimdonghee.account.auth.user.repositories import find_user
from com.kimdonghee.utils.creational.abstract.abstract_service import AbstractService


class Login(AbstractService):
    async def handle(self, **kwargs):
        print("🎁🎁🎁🎀login진입함")
        print(kwargs)
        user_schema = kwargs.get("user_schema")
        print("🎁🎁🎁🎀user_schema진입", user_schema)
        db = kwargs.get("db")

        await find_user(user_schema=user_schema, db=db)


