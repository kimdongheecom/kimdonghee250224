

from com.kimdonghee.account.staff.manager.services.strategy_type import StrategyType
from com.kimdonghee.account.staff.manager.web.manager_factory import ManagerFactory


class ManagerController:
    def __init__(self):
        pass
    
    async def create_manager(self, **kwargs):
        return await ManagerFactory.execute(StrategyType.DEFAULT_CREATE,method="create", **kwargs)
    
    async def get_manager_detail(self, **kwargs):
        return await ManagerFactory.execute(StrategyType.GET_DETAIL,method="retrieve", **kwargs)
    
    async def get_manager_list(self,**kwargs): #kwargs는 db와 new_customer 두개를 의미함.
        return await ManagerFactory.execute(StrategyType.GET_ALL,method="retrieve", **kwargs)
    
    async def update_manager(self, **kwargs):
        return await ManagerFactory.execute(StrategyType.FULL_UPDATE,method="update", **kwargs)
    
    async def delete_manager(self, **kwargs):
        return await ManagerFactory.execute(StrategyType.HARD_DELETE,method="delete", **kwargs)
    
    
    

