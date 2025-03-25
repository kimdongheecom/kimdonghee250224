from datetime import datetime
from select import select
from com.kimdonghee.account.auth.user.models.user_entity import UserEntity
from com.kimdonghee.account.auth.user.models.user_schema import UserSchema


async def create_new_user(new_user: UserSchema):

    return UserEntity(
        user_id=new_user.user_id,
        email=new_user.email,
        password=new_user.password, 
        name=new_user.name,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )


async def get_user_by_id(user_id: str):
    return select(UserEntity).where(UserEntity.user_id == user_id)


async def get_user_by_email(email: str):
    return select(UserEntity).where(UserEntity.email == email)


async def get_user_by_name(name: str):
    return select(UserEntity).where(UserEntity.name == name)



