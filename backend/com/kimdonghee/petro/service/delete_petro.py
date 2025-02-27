




from com.kimdonghee.petro.service.abstract_petro import AbstractPetro


class DeletePetro(AbstractPetro):
    
    def handle(self, **kwargs):
        return "Delete Petro"
