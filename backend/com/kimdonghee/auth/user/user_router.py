from fastapi import APIRouter

from com.kimdonghee.auth.user.user_service import UserService


router = APIRouter()
user_service = UserService()

@router.get("/")

def hello():    
      return user_service.hello()

def add_user(user):
      print(f"➕컨트롤러 추가:{user}")
      return UserService().hello()

def get_user(user):
      print(f"❓컨트롤러 조회:{user}")
      return UserService().hello()

def update_user(user):
      print(f"❗컨트롤러 수정:{user}")
      return UserService().hello()

def delete_user(self,user):
      print(f"❌컨트롤러 삭제:{user}")
      return UserService().hello()

