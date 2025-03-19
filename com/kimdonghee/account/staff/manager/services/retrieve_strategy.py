from multiprocessing import managers
from com.kimdonghee.account.staff.manager.service.retrieve_service import RetrieveService
from sqlalchemy.ext.asyncio import AsyncSession

class GetAllStrategy(RetrieveService):
    async def retrieve(self, db: AsyncSession, **kwargs):
        try:
            query = "SELECT user_id, email, name FROM member"
            result = await db.fetch(query)

            managers = [
                {
                    "id": row["user_id"],
                    "email": row["email"],
                    "name": row["name"]
                }
                for row in result
            ]

            return {"managers": managers, "count": len(managers)}
        except Exception as e:
            print(f"⚠️ 데이터 조회 중 오류 발생:, {str(e)}")
            return {"managers": [], "count": 0, "error": str(e)}
    
class GetDetailStrategy(RetrieveService):
    async def retrieve(self,db:AsyncSession,**kwargs):
        pass