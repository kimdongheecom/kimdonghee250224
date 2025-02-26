
      
from fastapi import APIRouter

from com.kimdonghee.auth.admin.admin_service import AdminService


router = APIRouter()
admin_service = AdminService()

@router.get("/")
def hello():    
      return admin_service.hello()

def add_admin(self,admin):
      print(f"➕컨트롤러 추가:{admin}")
      return admin

def get_admin(self,admin):
      print(f"❓컨트롤러 조회:{admin}")
      return admin

def update_admin(self,admin):
      print(f"❗컨트롤러 수정:{admin}")
      return admin

def delete_admin(self,admin):
      print(f"❌컨트롤러 삭제:{admin}")
      return "Success"