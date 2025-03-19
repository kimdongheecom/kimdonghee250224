from sqlalchemy.ext.asyncio import AsyncSession

from com.kimdonghee.account.guest.customer.models.customer_schema import CustomerSchema
from com.kimdonghee.account.guest.customer.storages.find_customer_query import GetAllRepository, GetDetailRepository
from com.kimdonghee.utils.creational.abstract.abstract_service import AbstractService

class FindCustomers(AbstractService):

    async def handle(self, db: AsyncSession, **kwargs):
        pass