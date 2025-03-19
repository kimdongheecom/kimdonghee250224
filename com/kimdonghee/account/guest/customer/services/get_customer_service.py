from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from com.kimdonghee.account.guest.customer.storages.get_customer_query import get_all_customers
from com.kimdonghee.utils.creational.abstract.abstract_service import AbstractService

class GetAllCustomers(AbstractService):

    async def handle(self, **kwargs):
        db = kwargs.get("db")
        try:
            # begin() 메서드 사용 대신 직접 쿼리 실행
            customers = await get_all_customers(db)
            
            # 결과 형식 표준화
            if isinstance(customers, list):
                return {"customers": customers, "count": len(customers)}
            elif hasattr(customers, '__len__'):  # asyncpg.Record 객체 리스트인 경우
                customer_list = [dict(record) for record in customers]
                return {"customers": customer_list, "count": len(customer_list)}
            else:
                return customers  # 이미 적절한 형식으로 반환된 경우
        except Exception as e:
            print(f"[ERROR] GetAllCustomers failed: {str(e)}")
            return {"error": "Failed to retrieve customer data.", "details": str(e)}

class GetCustomerById(AbstractService):

    async def handle(self, db: AsyncSession, **kwargs):
        pass