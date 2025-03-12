

from com.kimdonghee.account.guest.customer.model.customer_schema import CustomerSchema
from com.kimdonghee.account.guest.subscriber.service.update_service import UpdateService
from sqlalchemy.ext.asyncio import AsyncSession

class FullUpdateStrategy(UpdateService): #전체 업데이트
    
    def update(self, db:AsyncSession,update_customer:CustomerSchema):
        pass
class PartialUpdateStrategy(UpdateService): #부분 업데이트
    
    def update(self,db:AsyncSession,update_customer:CustomerSchema):
        pass