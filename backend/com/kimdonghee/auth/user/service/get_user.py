


from com.kimdonghee.auth.user.service.abstract_user import AbstractUser


class GetUser(AbstractUser):
    
 
     def handle(self, **kwargs):
        return "Get User"

