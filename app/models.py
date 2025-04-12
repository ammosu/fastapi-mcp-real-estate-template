from sqlalchemy import Column, String, Integer, Float, Date
from sqlalchemy.dialects.postgresql import UUID
from .database import Base

class RealEstateData(Base):
    __tablename__ = "real_estate_data"

    transaction_id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    transaction_date = Column(Date, nullable=False)
    city = Column(String(50))
    district = Column(String(50))
    address = Column(String(200))
    building_type = Column(String(50))
    price = Column(Integer)
    building_area = Column(Float)
    unit_price = Column(Float)
    floor_level = Column(Integer)
    building_age = Column(Float)
    total_floors = Column(Integer)
    land_area = Column(Float)
    main_use = Column(String(100))
    construction_materials = Column(String(100))
    transaction_type = Column(String(50))

class APIKey(Base):
    __tablename__ = "api_keys"
    id = Column(Integer, primary_key=True, autoincrement=True)
    key = Column(String(128), unique=True, nullable=False, index=True)
    owner = Column(String(100), nullable=True)
    is_active = Column(Integer, default=1)  # 1: 有效, 0: 停用
    usage_count = Column(Integer, default=0)  # 可用於記錄使用次數
    # 可擴充更多欄位（如點數、到期日等）