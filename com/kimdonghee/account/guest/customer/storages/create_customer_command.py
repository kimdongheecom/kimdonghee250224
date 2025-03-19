

from com.kimdonghee.account.guest.customer.models.customer_entity import CustomerEntity
from com.kimdonghee.account.guest.customer.models.customer_schema import CustomerSchema


    
    
async def create_customer(new_customer:CustomerSchema): #db먼저 넣었으면, 그 다음 new를 넣어줘야한다. 안그러면 오류남. db 옆에다가 넣으면 안된다.
        
        return CustomerEntity(
            user_id=new_customer.user_id,
            name=new_customer.name,
            email=new_customer.email,
            password=new_customer.password,
        )

