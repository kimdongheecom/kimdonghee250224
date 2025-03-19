from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from com.kimdonghee.account.guest.customer.api.customer_controller import CustomerController
from com.kimdonghee.account.guest.customer.models.customer_schema import CustomerSchema
from com.kimdonghee.utils.creational.builder.db_builder import get_db



router = APIRouter()
controller = CustomerController()

@router.post(path="/create")
async def create_customer(new_customer:CustomerSchema, db: AsyncSession = Depends(get_db)):
    print("🎋🎄🎍", "create_customer 로 진입함")
    print("new_customer", new_customer)
    return await controller.create_customer(new_customer=new_customer, db=db)
    
@router.get(path="/detail")
async def get_customer_by_id():
    return await controller.get_customer_by_id()

@router.get(path="/list")
async def get_all_customers(db:AsyncSession=Depends(get_db)):
    return await controller.get_all_customers(db=db)

@router.put(path="/update")
async def update_customer():
    return await controller.update_customer()

@router.delete(path="/delete")
async def delete_customer():
    return await controller.delete_customer()


