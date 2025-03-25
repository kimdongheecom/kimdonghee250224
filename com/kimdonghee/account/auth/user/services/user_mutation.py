from com.kimdonghee.utils.creational.abstract.abstract_service import AbstractService


class CreateNewUser(AbstractService):
    
    async def handle(self, **kwargs):
        db = kwargs.get("db")
        user_schema = kwargs.get("user_schema")
        try:
            pass
        except Exception as e:
            return "fail"
