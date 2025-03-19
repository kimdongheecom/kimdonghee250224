from typing import Literal
from sqlalchemy.ext.asyncio import AsyncSession

from com.kimdonghee.account.guest.customer.models.customer_action import CustomerAction
from com.kimdonghee.account.guest.customer.services.create_customer_service import CreateCustomer
from com.kimdonghee.account.guest.customer.services.delete_customer_service import DeleteCustomer, RemoveCustomer
from com.kimdonghee.account.guest.customer.services.get_customer_service import GetAllCustomers, GetCustomerById
from com.kimdonghee.account.guest.customer.services.update_customer_service import PatchCustomer, UpdateCustomer



class CustomerFactory:

    _strategy_map = {
        CustomerAction.CREATE_CUSTOMER: CreateCustomer(),
        CustomerAction.DELETE_CUSTOMER: DeleteCustomer(),
        CustomerAction.REMOVE_CUSTOMER: RemoveCustomer(),
        CustomerAction.GET_ALL_CUSTOMERS: GetAllCustomers(),
        CustomerAction.GET_CUSTOMER_BY_ID: GetCustomerById(),
        CustomerAction.UPDATE_CUSTOMER: UpdateCustomer(),
        CustomerAction.PATCH_CUSTOMER: PatchCustomer(),
    }
       

    @staticmethod
    async def create(strategy, **kwargs):
        instance = CustomerFactory._strategy_map[strategy]
        if not instance:
            raise Exception("invalid strategy")
        return await instance.handle(**kwargs)