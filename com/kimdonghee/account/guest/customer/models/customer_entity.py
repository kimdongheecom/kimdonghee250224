from com.kimdonghee.account.common.user.model.user_entity import UserEntity

class CustomerEntity(UserEntity):
    """
    고객 엔티티 클래스. UserEntity를 상속받아 회원 정보를 확장합니다.
    """
    def __init__(self, user_id: str, email: str, password: str, name: str):
        super().__init__(user_id=user_id, email=email, password=password, name=name)

    


