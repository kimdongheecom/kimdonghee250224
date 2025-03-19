from fastapi import APIRouter

from com.kimdonghee.account.guest.customer.api.customer_router import router as customer_router
from com.kimdonghee.account.staff.manager.web.manager_router import router as manager_router

router = APIRouter()

router.include_router(customer_router, prefix="/customer") #router는 서브라우터이다.
router.include_router(manager_router, prefix="/manager")
print("😎😀➕ 어카운트 라우터로 진입")