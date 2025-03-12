
from com.kimdonghee.account.guest.customer.model.customer_schema import CustomerSchema

from com.kimdonghee.account.guest.customer.repository.create_repository import DefaultCreateRepository
from com.kimdonghee.account.guest.customer.service.create_service import CreateService
from sqlalchemy.ext.asyncio import AsyncSession

class DefaultCreateCustomerStrategy(CreateService):
    async def create(self, db: AsyncSession, new_customer: CustomerSchema) :
        customer_repo = DefaultCreateRepository(db)
        return customer_repo.create(new_customer)

class ValidateCreateCustomerStrategy(CreateService):
    
    async def create(self,db:AsyncSession,new_customer:CustomerSchema):
        pass
