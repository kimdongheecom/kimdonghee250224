from com.kimdonghee.auth.admin.service.abstract_admin import AbstractAdmin


class DeleteAdmin(AbstractAdmin):
 
    def handle(self, **kwargs):
        return "Delete Admin"

