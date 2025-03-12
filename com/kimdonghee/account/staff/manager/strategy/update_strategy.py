

from com.kimdonghee.account.staff.manager.model.manager_schema import ManagerSchema
from com.kimdonghee.account.staff.manager.service.update_service import UpdateService
from sqlalchemy.ext.asyncio import AsyncSession

class FullUpdateStrategy(UpdateService): #전체 업데이트
    
    def update(self, db:AsyncSession,update_manager:ManagerSchema):
        pass
class PartialUpdateStrategy(UpdateService): #부분 업데이트
    
    def update(self,db:AsyncSession,update_manager:ManagerSchema):
        pass