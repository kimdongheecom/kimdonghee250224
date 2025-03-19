from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text

from com.kimdonghee.account.guest.customer.models.customer_schema import CustomerSchema


async def find_customers(db: AsyncSession, schema: CustomerSchema):
    query = text("SELECT * FROM member")
    try:
            result = await db.execute(query)
            records = result.fetchall()
            return [dict(record._mapping) for record in records]
    except SQLAlchemyError as e:
        print("⚠️ 데이터 조회 중 오류 발생:", str(e))
        raise e