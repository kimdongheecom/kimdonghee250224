from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession

from com.kimdonghee.account.staff.manager.model.manager_schema import ManagerSchema


class UpdateService(ABC): #추상화 패턴 사용. 왜냐하면 추상화는 method를 재사용 할 때, 
    
    @abstractmethod
    async def update(self,db:AsyncSession,update_manager:ManagerSchema):
        pass