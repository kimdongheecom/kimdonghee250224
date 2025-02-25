class UserController:
      
      def __init__(self):
            pass

      def add_user(self,user):
            print(f"➕컨트롤러 추가:{user}")
            return user
      
      def get_user(self,user):
            print(f"❓컨트롤러 조회:{user}")
            return user
      
      def update_user(self,user):
            print(f"❗컨트롤러 수정:{user}")
            return user
      
      def delete_user(self,user):
            print(f"❌컨트롤러 삭제:{user}")
            return "Success"
      
