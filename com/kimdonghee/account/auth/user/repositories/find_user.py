from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import Result, select, func, text
from com.kimdonghee.account.auth.user.models.user_entity import UserEntity

def get_check_user_id_stmt(user_id: str):
    return text("""
        SELECT 1 FROM users
        WHERE user_id = :user_id
        LIMIT 1
    """), {"user_id": user_id}


def get_login_stmt(user_id: str, password: str):
    return text("""
        SELECT * FROM users
        WHERE user_id = :user_id AND password = :password
        LIMIT 1
    """), {
        "user_id": user_id,
        "password": password
    }



# postgresql을 사용함. 이후 로직은 alchemy의 core로 작성함. 