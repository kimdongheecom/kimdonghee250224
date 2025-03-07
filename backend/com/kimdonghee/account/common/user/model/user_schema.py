from pydantic import BaseModel, EmailStr, SecretStr

# 기본 유저 데이터 모델 (공통 속성)
class MemberBase(BaseModel):
    user_id: str
    email: EmailStr
    name: str

# 유저 생성 요청 모델 (비밀번호 포함)
class MemberCreate(MemberBase):
    password: SecretStr  # 비밀번호 보안을 위해 SecretStr 사용

# 유저 응답 모델 (비밀번호 제외)
class MemberResponse(MemberBase):
    class Config:
        from_attributes = True  # ORM과 호환 가능


    
    


