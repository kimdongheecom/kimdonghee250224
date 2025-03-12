from sqlalchemy.ext.asyncio import AsyncSession

from com.kimdonghee.account.staff.manager.model.manager_entity import ManagerEntity
from com.kimdonghee.account.staff.manager.model.manager_schema import ManagerSchema
from com.kimdonghee.account.staff.manager.service.create_service import CreateService

class DefaultCreateRepository(CreateService):
    async def create(self,db:AsyncSession,new_customer:ManagerSchema): #db먼저 넣었으면, 그 다음 new를 넣어줘야한다. 안그러면 오류남. db 옆에다가 넣으면 안된다.
        db.add(ManagerEntity(
            user_id=new_customer.user_id,
            name=new_customer.name,
            email=new_customer.email,
            password=new_customer.password,
        ))
        db.commit() #커밋은 저장하는 것, 카톡 샌드가 커밋이다.
        db.refresh(new_customer) #리프레쉬: 새로고침
        return await new_customer #리턴은 회원가입창에서 

class ValidateCreateRepository(CreateService):   
    async def create(self,db:AsyncSession,new_manager:ManagerSchema):
        print("🎆🎇🎈Repository new_manager:", new_manager)
        pass
