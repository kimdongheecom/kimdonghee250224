from fastapi import APIRouter

from com.kimdonghee.account.account_router import router as account_router


router = APIRouter()

router.include_router(account_router) #router는 서브라우터이다.
print("😎😀➕ 앱 라우터로 진입")


