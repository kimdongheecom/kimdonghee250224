

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from com.kimdonghee.account.staff.manager.web.manager_controller import ManagerController
from com.kimdonghee.utils.creational.builder.db_builder import get_db



router = APIRouter()
controller = ManagerController()


@router.post(path="/create")
async def create_manager():
    return await controller.create_manager()
    

@router.get(path="/detail")
async def get_manager_detail():
    return await controller.get_manager_detail()

@router.get(path="/list")
async def get_manager_list(db:AsyncSession=Depends(get_db)):
    print("😎😀➕ get/manager로 진입")
    return await controller.get_manager_list(db=db)
    
@router.put(path="/update")
async def update_manager():
    return await controller.update_manager()

@router.delete(path="/delete")
async def delete_customer():
    return await controller.delete_manager()



