from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from uuid import UUID
from .. import models, schemas, database

router = APIRouter(
    prefix="/properties",
    tags=["properties"]
)

from fastapi.responses import JSONResponse
from datetime import datetime

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[schemas.RealEstateData])
def read_properties(
    city: Optional[str] = Query("新北市", example="新北市", description="城市"),
    district: Optional[str] = Query(None, example="板橋區", description="區域"),
    building_type: Optional[str] = Query(None, example="大樓", description="建物型態"),
    transaction_type: Optional[str] = Query(None, example="買賣", description="交易型態"),
    main_use: Optional[str] = Query(None, example="住家用", description="主用途"),
    construction_materials: Optional[str] = Query(None, example="鋼筋混凝土", description="建材"),
    min_price: Optional[int] = Query(None, example=10000000, description="最低總價"),
    max_price: Optional[int] = Query(None, example=20000000, description="最高總價"),
    min_unit_price: Optional[float] = Query(None, example=100000, description="最低單價"),
    max_unit_price: Optional[float] = Query(None, example=200000, description="最高單價"),
    min_building_area: Optional[float] = Query(None, example=50.0, description="最小建物面積"),
    max_building_area: Optional[float] = Query(None, example=100.0, description="最大建物面積"),
    min_floor_level: Optional[int] = Query(None, example=1, description="最低樓層"),
    max_floor_level: Optional[int] = Query(None, example=20, description="最高樓層"),
    min_building_age: Optional[float] = Query(None, example=0, description="最小屋齡"),
    max_building_age: Optional[float] = Query(None, example=30, description="最大屋齡"),
    min_transaction_date: Optional[str] = Query(None, example="2023-01-01", description="最早交易日期"),
    max_transaction_date: Optional[str] = Query(None, example="2024-12-31", description="最晚交易日期"),
    address_keyword: Optional[str] = Query(
        None,
        alias="address_contains",
        example="中山路",
        description="地址關鍵字（可用 address_contains 傳遞）"
    ),
    page: int = Query(1, ge=1, example=1, description="頁碼"),
    page_size: int = Query(20, ge=1, le=100, example=20, description="每頁筆數"),
    db: Session = Depends(get_db)
):
    query = db.query(models.RealEstateData)
    if city:
        query = query.filter(models.RealEstateData.city == city)
    if district:
        query = query.filter(models.RealEstateData.district == district)
    if building_type:
        query = query.filter(models.RealEstateData.building_type == building_type)
    if transaction_type:
        query = query.filter(models.RealEstateData.transaction_type == transaction_type)
    if main_use:
        query = query.filter(models.RealEstateData.main_use == main_use)
    if construction_materials:
        query = query.filter(models.RealEstateData.construction_materials == construction_materials)
    if min_price is not None:
        query = query.filter(models.RealEstateData.price >= min_price)
    if max_price is not None:
        query = query.filter(models.RealEstateData.price <= max_price)
    if min_unit_price is not None:
        query = query.filter(models.RealEstateData.unit_price >= min_unit_price)
    if max_unit_price is not None:
        query = query.filter(models.RealEstateData.unit_price <= max_unit_price)
    if min_building_area is not None:
        query = query.filter(models.RealEstateData.building_area >= min_building_area)
    if max_building_area is not None:
        query = query.filter(models.RealEstateData.building_area <= max_building_area)
    if min_floor_level is not None:
        query = query.filter(models.RealEstateData.floor_level >= min_floor_level)
    if max_floor_level is not None:
        query = query.filter(models.RealEstateData.floor_level <= max_floor_level)
    if min_building_age is not None:
        query = query.filter(models.RealEstateData.building_age >= min_building_age)
    if max_building_age is not None:
        query = query.filter(models.RealEstateData.building_age <= max_building_age)
    if min_transaction_date is not None:
        query = query.filter(models.RealEstateData.transaction_date >= min_transaction_date)
    if max_transaction_date is not None:
        query = query.filter(models.RealEstateData.transaction_date <= max_transaction_date)
    if address_keyword:
        query = query.filter(models.RealEstateData.address.contains(address_keyword))
    # 分頁
    offset = (page - 1) * page_size
    results = query.offset(offset).limit(page_size).all()
    return results

@router.get("/now")
def get_now():
    """取得現在時間（ISO 格式）"""
    return JSONResponse(content={"now": datetime.now().isoformat()})

@router.get("/{transaction_id}", response_model=schemas.RealEstateData)
def read_property(transaction_id: UUID, db: Session = Depends(get_db)):
    property = db.query(models.RealEstateData).filter(models.RealEstateData.transaction_id == transaction_id).first()
    if not property:
        raise HTTPException(status_code=404, detail="Property not found")
    return property