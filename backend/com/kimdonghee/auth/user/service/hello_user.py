
from com.kimdonghee.auth.user.service.abstract_user import AbstractUser


class HelloUser(AbstractUser):
    
 
    def handle(self, **kwargs): #@abstractmethod가 없으면 구상이다. 
        return "Hello User"