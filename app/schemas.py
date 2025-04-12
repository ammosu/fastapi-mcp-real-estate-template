from typing import Optional
from datetime import date
from uuid import UUID
from pydantic import BaseModel

class RealEstateDataBase(BaseModel):
    transaction_date: date
    city: Optional[str]
    district: Optional[str]
    address: Optional[str]
    building_type: Optional[str]
    price: Optional[int]
    building_area: Optional[float]
    unit_price: Optional[float]
    floor_level: Optional[int]
    building_age: Optional[float]
    total_floors: Optional[int]
    land_area: Optional[float]
    main_use: Optional[str]
    construction_materials: Optional[str]
    transaction_type: Optional[str]

class RealEstateData(RealEstateDataBase):
    transaction_id: UUID

    class Config:
        orm_mode = True

class RealEstateDataQuery(BaseModel):
    city: Optional[str]
    district: Optional[str]
    building_type: Optional[str]
    transaction_type: Optional[str]
    main_use: Optional[str]
    construction_materials: Optional[str]
    min_price: Optional[int]
    max_price: Optional[int]
    min_unit_price: Optional[float]
    max_unit_price: Optional[float]
    min_building_area: Optional[float]
    max_building_area: Optional[float]
    min_floor_level: Optional[int]
    max_floor_level: Optional[int]
    min_building_age: Optional[float]
    max_building_age: Optional[float]
    min_transaction_date: Optional[date]
    max_transaction_date: Optional[date]
    address_keyword: Optional[str]
    page: Optional[int] = 1
    page_size: Optional[int] = 20