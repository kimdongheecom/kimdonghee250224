from dataclasses import dataclass

@dataclass
class SubscriberSchema:
    email:str
    password:str
    username:str

    @property
    def id(self) -> object:
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
    
    @property
    def password(self) -> object:
        return self._password
    
    @password.setter
    def password(self, password):
        self._password = password
    
    @property
    def username(self) -> object:
        return self._username
    
    @username.setter
    def username(self, username):
        self._username = username

    
    


