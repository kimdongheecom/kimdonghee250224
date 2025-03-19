from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text

async def get_all_customers(db):
    """
    데이터베이스에서 모든 고객 정보를 가져옵니다.
    
    Args:
        db: AsyncDatabase 또는 AsyncSession 객체
        
    Returns:
        고객 정보 목록
    """
    # 직접 문자열 쿼리 사용
    query = "SELECT * FROM member"
    try:
        # db가 AsyncDatabase 또는 AsyncSession인지 확인
        if hasattr(db, 'fetch'):  # AsyncDatabase
            result = await db.fetch(query)
            # asyncpg는 직접 딕셔너리로 변환 가능
            return result
        else:  # AsyncSession
            result = await db.execute(text(query))
            records = result.fetchall()
            # 결과를 리스트로 변환하여 연결 의존성 제거
            return [dict(record._mapping) for record in records]
    except Exception as e:
        print(f"⚠️ 데이터 조회 중 오류 발생: {str(e)}")
        raise e



async def get_customer_by_id(self, db, user_id: str):
    pass