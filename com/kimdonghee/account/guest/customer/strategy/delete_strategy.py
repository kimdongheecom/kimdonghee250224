from com.kimdonghee.account.guest.customer.model.customer_schema import CustomerSchema
from com.kimdonghee.account.guest.customer.service.delete_service import DeleteService
from sqlalchemy.orm import Session


class SoftDeleteCustomerStrategy(DeleteService): #삭제가 진짜로 된건 아니고, 휴면계정으로 바꿀때......
    
    async def delete(self, db:Session,new_customer:CustomerSchema):
        pass
class HardDeleteCustomerStrategy(DeleteService): #정말 삭제된 경우
    
    async def delete(self,db:Session,new_customer:CustomerSchema):
        pass