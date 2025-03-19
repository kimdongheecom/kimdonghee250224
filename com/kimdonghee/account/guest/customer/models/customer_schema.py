from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class CustomerSchema(BaseModel):
    user_id: str = Field(..., description="사용자 아이디", min_length=3, max_length=20)
    email: EmailStr = Field(..., description="사용자 이메일")
    password: str = Field(..., description="사용자 비밀번호", min_length=6)
    name: str = Field(..., description="사용자 이름")
    
    class Config:
        title = "고객 스키마"
        
