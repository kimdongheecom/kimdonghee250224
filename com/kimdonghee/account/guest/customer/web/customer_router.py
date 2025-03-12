from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from com.kimdonghee.account.guest.customer.web.customer_controller import CustomerController
from com.kimdonghee.utils.creational.builder.db_builder import get_db


router = APIRouter()
controller = CustomerController()

@router.post(path="/create")
async def create_customer():
    return controller.create_customer()
    
@router.get(path="/detail")
async def get_customer_detail():
    return controller.get_customer_detail()

@router.get(path="/list")
async def get_customer_list(db:AsyncSession=Depends(get_db)):
    return await controller.get_customer_list(db=db)

@router.put(path="/update")
async def update_customer():
    return controller.update_customer()

@router.delete(path="/delete")
async def delete_customer():
    return controller.delete_customer()


