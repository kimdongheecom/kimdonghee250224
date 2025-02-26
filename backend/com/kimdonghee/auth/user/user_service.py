class UserService:
    
    def __init__(self):
        pass

    def hello(self):
        print( "Hello: World!" )
        return {"서비스": "서비스 호출됨"}


    def add_user(self,user):
        print(f"➕사용자 추가:{user}")
        return user
    
    def get_user(self,user):
        print(f"❓사용자 조회:{user}")
        return user
    
    def update_user(self,user):
        print(f"❗사용자 수정:{user}")
        return user
    
    def delete_user(self,user):
        print(f"❌사용자 삭제:{user}")
        return "Success"
    
