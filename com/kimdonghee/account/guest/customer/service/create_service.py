from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession

from com.kimdonghee.account.guest.customer.model.customer_schema import CustomerSchema


class CreateService(ABC): #추상화 패턴 사용. 왜냐하면 추상화는 method를 재사용 할 때, 
    
    @abstractmethod
    async def create(self,db:AsyncSession, new_customer:CustomerSchema):
        pass


