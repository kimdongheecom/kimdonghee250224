from fastapi import APIRouter
from com.kimdonghee.auth.admin.web.admin_controller import AdminController


router = APIRouter()
controller = AdminController()

@router.get(path= "/")
async def add_admin():
    return controller.add_admin()