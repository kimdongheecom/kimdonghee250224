


from com.kimdonghee.auth.admin.service.add_admin import AddAdmin


strategy_map = {
    "add_admin": AddAdmin(), #키가 있으면, 
}

class AdminFactory:

    @staticmethod
    def create(strategy: str, **kwargs):
        instance = strategy_map[strategy]
        if not instance:
            raise Exception("Invalid strategy")
        return instance.handle(**kwargs)