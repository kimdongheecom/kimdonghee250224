from com.kimdonghee.petro.service.add_petro import AddPetro


strategy_map = {
    "add_petro": AddPetro(), #키가 있으면, 
}

class PetroFactory:

    @staticmethod
    def create(strategy: str, **kwargs):
        instance = strategy_map[strategy]
        if not instance:
            raise Exception("Invalid strategy")
        return instance.handle(**kwargs)