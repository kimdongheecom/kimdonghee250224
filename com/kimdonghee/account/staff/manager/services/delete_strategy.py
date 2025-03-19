from com.kimdonghee.account.staff.manager.model.manager_schema import ManagerSchema
from com.kimdonghee.account.staff.manager.service.delete_service import DeleteService
from sqlalchemy.ext.asyncio import AsyncSession

class SoftDeleteManagerStrategy(DeleteService): #삭제가 진짜로 된건 아니고, 휴면계정으로 바꿀때......
    
    async def delete(self, db:AsyncSession,new_manager:ManagerSchema):
        pass
class HardDeleteManagerStrategy(DeleteService): #정말 삭제된 경우
    
    async def delete(self,db:AsyncSession,new_manager:ManagerSchema):
        pass