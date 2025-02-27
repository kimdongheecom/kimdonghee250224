
from com.kimdonghee.auth.user.service.abstract_user import AbstractUser

class GetAllUser(AbstractUser):
    
 
     def handle(self, **kwargs):
        return "Get All User"

