from com.kimdonghee.account.guest.customer.models.customer_schema import CustomerSchema

from sqlalchemy.ext.asyncio import AsyncSession

from com.kimdonghee.utils.creational.abstract.abstract_service import AbstractService


class DeleteCustomer(AbstractService): #삭제가 진짜로 된건 아니고, 휴면계정으로 바꿀때...... 
    async def handle(self, db:AsyncSession,user_id:str):
        pass

class RemoveCustomer(AbstractService):
    async def handle(self,db:AsyncSession,user_id:str):
        pass
