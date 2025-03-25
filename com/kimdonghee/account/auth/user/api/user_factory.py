
from com.kimdonghee.account.auth.user.models.user_action import UserAction
from com.kimdonghee.account.auth.user.services.user_lookup import Login




class UserFactory:

    _strategy_map = {
        UserAction.LOGIN: Login(),
    }
       

    @staticmethod
    async def create(strategy, **kwargs):
        instance = UserFactory._strategy_map[strategy]
        if not instance:
            raise Exception("invalid strategy")
        return await instance.handle(**kwargs)