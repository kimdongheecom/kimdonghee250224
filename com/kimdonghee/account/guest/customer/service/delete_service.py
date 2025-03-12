from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession




class DeleteService(ABC): #추상화 패턴 사용. 왜냐하면 추상화는 method를 재사용 할 때, 
    
    @abstractmethod
    async def delete(self,db:AsyncSession,user_id:str):
        pass