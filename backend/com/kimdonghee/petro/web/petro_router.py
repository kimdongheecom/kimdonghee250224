from fastapi import APIRouter

from com.kimdonghee.petro.web.petro_controller import PetroController


router = APIRouter()
controller = PetroController()

@router.get(path= "/")
async def add_petro():
    return controller.add_petro()