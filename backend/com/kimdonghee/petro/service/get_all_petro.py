from com.kimdonghee.auth.admin.service.abstract_admin import AbstractAdmin
from com.kimdonghee.petro.service.abstract_petro import AbstractPetro


class GetAllPetro(AbstractPetro):
    
    def handle(self, **kwargs):
        return "Get All Petro"


