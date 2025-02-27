
from com.kimdonghee.auth.user.service.abstract_user import AbstractUser


class DeleteUser(AbstractUser):
    
     def handle(self, **kwargs):
        return "Delete User"

