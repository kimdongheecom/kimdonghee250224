from com.kimdonghee.auth.user.service.abstract_user import AbstractUser


class AddUser(AbstractUser): #자식 클래스 = "서브 클래스" 추상클래스의 자식들을 스트레티지라고 한다. 
    
    def handle(self, **kwargs): #@abstractmethod가 없으면 구상이다. 
        return "Add User"


    
