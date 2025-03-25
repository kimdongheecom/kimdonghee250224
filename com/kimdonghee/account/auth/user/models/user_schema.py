from pydantic import BaseModel, EmailStr

# 기본 유저 데이터 모델 (공통 속성)
class UserSchema(BaseModel):
    user_id: str
    email: EmailStr
    name: str
    password: str
    class Config:
        from_attributes = True

# 로그인을 위한 스키마 추가
class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str
    class Config:
        from_attributes = True

# # 유저 생성 요청 모델 (비밀번호 포함)
# class MemberCreate(MemberBase):
#     password: SecretStr  # 비밀번호 보안을 위해 SecretStr 사용

# # 유저 응답 모델 (비밀번호 제외)
# class MemberResponse(MemberBase):
#     class Config:
#         from_attributes = True  # ORM과 호환 가능


    
    


