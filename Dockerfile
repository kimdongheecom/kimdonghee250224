# 1. 공식 Python 이미지 사용 #Dockerfile은 확장자이다.
FROM python:3.12.7-slim

# 2. 작업 디렉토리 설정
WORKDIR /com/kimdonghee

# 3. 필요한 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 애플리케이션 코드 복사
COPY . /com/kimdonghee

# 5. FastAPI 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
