from dataclasses import dataclass

from com.kimdonghee.account.common.user.model.user_schema import UserSchema

@dataclass
class CustomerSchema(UserSchema): #상속: property 재사용
    pass


    


