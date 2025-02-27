
from com.kimdonghee.auth.admin.web.admin_factory import AdminFactory


class AdminController:
    def __init__(self):
        pass

    def add_admin(self, **kwargs):
        return AdminFactory.create(strategy="add_admin", **kwargs)