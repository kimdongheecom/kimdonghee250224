


from com.kimdonghee.petro.service.abstract_petro import AbstractPetro


class GetPetro(AbstractPetro):
    
    def handle(self, **kwargs):
        return "Get Petro"
