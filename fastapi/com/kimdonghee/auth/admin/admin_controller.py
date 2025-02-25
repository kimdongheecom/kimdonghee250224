class AdminController:
      
      def __init__(self):
            pass

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