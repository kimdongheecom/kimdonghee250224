from com.kimdonghee.auth.admin.service.abstract_admin import AbstractAdmin


class GetAllUser(AbstractAdmin):
    
 
     def handle(self, **kwargs):
        return "Get All Admin"

