
from com.kimdonghee.account.staff.manager.model.manager_schema import ManagerSchema
from com.kimdonghee.account.staff.manager.repository.create_repository import DefaultCreateRepository
from com.kimdonghee.account.staff.manager.service.create_service import CreateService
from sqlalchemy.ext.asyncio import AsyncSession

class DefaultCreateManagerStrategy(CreateService):
    
    
    async def create(self,db:AsyncSession,new_customer:ManagerSchema): #db먼저 넣었으면, 그 다음 new를 넣어줘야한다. 안그러면 오류남. db 옆에다가 넣으면 안된다.
        manager_repo = DefaultCreateRepository(db)
        return manager_repo.create(new_customer)
class ValidateCreateManagerStrategy(CreateService):
    
    async def create(self,db:AsyncSession,new_manager:ManagerSchema):
        pass
