from com.kimdonghee.petro.web.petro_factory import PetroFactory


class PetroController:
    
    def __init__(self):
        pass

    def add_petro(self, **kwargs):
        return PetroFactory.create(strategy="add_petro", **kwargs)