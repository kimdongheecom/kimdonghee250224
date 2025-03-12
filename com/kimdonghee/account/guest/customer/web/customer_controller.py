
from com.kimdonghee.account.guest.customer.strategy.strategy_type import StrategyType
from com.kimdonghee.account.guest.customer.web.customer_factory import CustomerFactory


class CustomerController:
    def __init__(self):
        pass

    async def create_customer(self, **kwargs):
        return await CustomerFactory.execute(StrategyType.DEFAULT_CREATE,method="create", **kwargs) #default_create를 create 방식으로 해주세요.
    
    async def get_customer_detail(self, **kwargs):
        return await CustomerFactory.execute(StrategyType.GET_DETAIL,method="retrieve", **kwargs)
    
    async def get_customer_list(self, **kwargs):
        return await CustomerFactory.execute(StrategyType.GET_ALL,method="retrieve",**kwargs)
        
    async def update_customer(self, **kwargs):
        return await CustomerFactory.execute(StrategyType.FULL_UPDATE,method="update", **kwargs)
    
    async def delete_customer(self, **kwargs):
        return await CustomerFactory.execute(StrategyType.HARD_DELETE,method="delete", **kwargs)
