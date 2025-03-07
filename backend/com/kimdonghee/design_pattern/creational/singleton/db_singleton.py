import os
from threading import Lock

from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

class DataBaseSingleton:
    """데이터베이스 싱글톤 클래스"""
    
    _instance = None
    _lock = Lock()  # :white_check_mark: 멀티스레드 환경에서도 안전하게 인스턴스를 생성하도록 락 사용

    def __new__(cls):
        """싱글톤 인스턴스 생성"""
        if not cls._instance:
            with cls._lock:  # :white_check_mark: 멀티스레드 환경에서 안전하게 인스턴스 생성
                if not cls._instance:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialize()
        return cls._instance
    
    def _initialize(self):
        """환경 변수 값을 로드하여 설정 초기화"""
        print("🎋🎄🎍",os.getenv("DB_HOSTNAME")) # 환경변수 확인용
        self.db_hostname = os.getenv("DB_HOSTNAME")
        self.db_username = os.getenv("DB_USERNAME")
        self.db_password = os.getenv("DB_PASSWORD")
        self.db_port = int(os.getenv("DB_PORT", 5432))
        self.db_database = os.getenv("DB_DATABASE")
        self.db_charset = os.getenv("DB_CHARSET", "utf8mb4")

        # ✅ 환경 변수 검증
        if None in (self.db_hostname, self.db_username, self.db_password, self.db_database):
            raise ValueError("⚠️ Database 환경 변수가 설정되지 않았습니다.")

         # ✅ `asyncpg`용 DSN 변경 (`postgresql://` 형식 사용)
        self.db_url = os.getenv("DB_URL")  # ✅ .env에서 직접 가져옴

        if not self.db_url:
            # ✅ DB_URL이 없으면 수동으로 생성
            self.db_url = f"postgresql://{self.db_username}:{self.db_password}@{self.db_hostname}:{self.db_port}/{self.db_database}"

        print(f"✅ Database URL: {self.db_url}")  # ✅ 디버깅용 출력

# ✅ 싱글톤 인스턴스 생성
db_singleton = DataBaseSingleton()
print("🎋🎄🎍",db_singleton.db_hostname)