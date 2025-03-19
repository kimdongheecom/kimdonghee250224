
from com.kimdonghee.account.guest.customer.models.customer_action import CustomerAction
from com.kimdonghee.account.guest.customer.api.customer_factory import CustomerFactory


class CustomerController:
    def __init__(self):
        pass

    async def create_customer(self, **kwargs):
        return await CustomerFactory.create(strategy=CustomerAction.CREATE_CUSTOMER,**kwargs) #default_create를 create 방식으로 해주세요.
    
    async def get_customer_by_id(self, **kwargs):
        return await CustomerFactory.create(strategy=CustomerAction.GET_CUSTOMER_BY_ID,**kwargs)
    
    async def get_all_customers(self, **kwargs):
        return await CustomerFactory.create(strategy=CustomerAction.GET_ALL_CUSTOMERS,**kwargs)
        
    async def update_customer(self, **kwargs):
        return await CustomerFactory.create(strategy=CustomerAction.UPDATE_CUSTOMER,**kwargs)
    
    async def delete_customer(self, **kwargs):
        return await CustomerFactory.create(strategy=CustomerAction.DELETE_CUSTOMER,**kwargs)
