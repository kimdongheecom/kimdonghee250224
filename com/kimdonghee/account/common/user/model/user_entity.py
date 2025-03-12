from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserEntity(Base): #fpvkwl
    __tablename__ = "member"  # SQL 테이블 이름 지정

    user_id = Column(String(15), primary_key=True)  # PRIMARY KEY
    email = Column(String(20), unique=True, nullable=False)  # UNIQUE + NOT NULL
    password = Column(String(15), nullable=False)  # NOT NULL
    name = Column(String(10), nullable=False)  # NOT NULL

    
    


