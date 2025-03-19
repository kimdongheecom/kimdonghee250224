from sqlalchemy.ext.asyncio import AsyncSession

from com.kimdonghee.account.guest.customer.models.customer_schema import CustomerSchema
from com.kimdonghee.utils.creational.abstract.abstract_service import AbstractService


class UpdateCustomer(AbstractService):

    async def handler(self,  db: AsyncSession, update_customer: CustomerSchema):
        print("🚀🤖DeleteRepository update_customer 정보 : ", update_customer)
       
        return None

class PatchCustomer(AbstractService):

    async def handler(self, db: AsyncSession, update_customer: CustomerSchema):
        pass