
from com.kimdonghee.account.guest.customer.models.customer_entity import CustomerEntity
from com.kimdonghee.account.guest.customer.models.customer_schema import CustomerSchema

from sqlalchemy.ext.asyncio import AsyncSession


from com.kimdonghee.account.guest.customer.storages.create_customer_command import create_customer
from com.kimdonghee.utils.creational.abstract.abstract_service import AbstractService

class CreateCustomer(AbstractService):
    async def handle(self, **kwargs) :
        db: AsyncSession = kwargs.get("db")
        schema: CustomerSchema = kwargs.get("new_customer")
        try:
            customer: CustomerEntity = await create_customer(schema)
            db.add(customer)
            await db.commit()
            await db.refresh(customer)
            return customer
        except Exception as e:
            print("customerCreate:", e)
            await db.rollback()
            raise e