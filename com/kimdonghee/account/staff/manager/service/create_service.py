from abc import ABC,abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession

from com.kimdonghee.account.staff.manager.model.manager_schema import ManagerSchema

class CreateService(ABC):
    
    @abstractmethod
    async def create(self,db:AsyncSession,new_manager:ManagerSchema):
        pass