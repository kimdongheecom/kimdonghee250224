

from com.kimdonghee.auth.user.service.hello_user import HelloUser


strategy_map = {
    "hello_user": HelloUser(), #키가 있으면, 
}

class UserFactory:

    @staticmethod
    def create(strategy: str, **kwargs):
        instance = strategy_map[strategy]
        if not instance:
            raise Exception("Invalid strategy")
        return instance.handle(**kwargs)
   
        