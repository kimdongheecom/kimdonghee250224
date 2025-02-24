from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}  # 딕셔너리 반환 #추상화: 화면(브라우저)에 글자만 준 것을 추상화라고 한다.
                                         # 추상화 먼저하고, 캡슐화한다. 캡슐화는 깡통만들기를 의미한다.캡슐화는 클래스를 만드는 것이다.