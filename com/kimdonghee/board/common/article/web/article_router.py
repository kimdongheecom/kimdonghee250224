

from fastapi import APIRouter, Depends

from com.kimdonghee.board.common.article.web.article_controller import ArticleController


router = APIRouter()
controller = ArticleController()


@router.post(path="/article/create")
async def create_article():
    return controller.article_list()


@router.get(path="/article/detail")
async def get_article_detail():
    return controller.article_list()



# @router.get("/article/list")
# async def get_article_list(db=Depends(get_db)):
#     print("😎😀➕ get/articles로 진입")

#     try:
#         # 비동기 데이터베이스 연결 생성
#         conn = await asyncpg.connect(db_singleton.db_url)
        
#         query = "SELECT * FROM member"
#         rows = await conn.fetch(query)
        
#         result = [dict(row) for row in rows]
    
#         await conn.close()
        
#         return result
#     except Exception as e:
#         print(f"⚠️ 데이터베이스 쿼리 실행 중 오류 발생: {str(e)}")
#         return {"error": str(e)}
    

@router.put(path="/article/update")
async def update_article():
    return controller.hello_article()


@router.delete(path="/article/delete")
async def delete_article():
    return controller.hello_article()




