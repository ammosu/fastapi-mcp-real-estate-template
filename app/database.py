from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# 載入 .env 檔案（本地開發用）
load_dotenv()
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os

# 優先從系統環境變數取得 DATABASE_URL，否則用預設值
DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql://postgres:mysecretpassword@localhost:5432/mydb"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()