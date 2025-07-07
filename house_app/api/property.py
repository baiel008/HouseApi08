from alembic.util import status
from dns.e164 import query
from fastapi import HTTPException, Depends, APIRouter, Query
from sqlalchemy.util import Properties

from house_app.db.models import Property, PropertyChoices
from house_app.db.schema import PropertyCreateSchema, PropertyOutSchema
from house_app.db.database import SessionLocal
from sqlalchemy.orm import Session
from typing import List, Optional, dataclass_transform



async def get_db():
    db = SessionLocal()
    try:
        yield  db
    finally:
        db.close()



property_router = APIRouter(prefix='/property', tags=['Property'])


@property_router.post('/', response_model=dict)
async def create_property(property: PropertyCreateSchema, db: Session = Depends(get_db)):
    property_db = Property(**property.dict())
    db.add(property_db)
    db.commit()
    db.refresh(property_db)
    return {'message': 'Saved'}


@property_router.get('/search/', response_model=List[PropertyOutSchema])
async def search_property(title: str, db: Session = Depends(get_db)):
    property_db = db.query(Property).filter(Property.title.ilike(f'%{title}%')).all()
    if not property_db:
        raise HTTPException(status_code=404, detail='Property not found')
    return property_db


@property_router.get('/', response_model=List[PropertyOutSchema])
async def property_list(
        min_price: Optional[float] = Query(None, alais='price[from]'),
        max_price: Optional[float] = Query(None, alais='price[to]'),
        min_floor: Optional[float] = Query(None, alais='floor[from]'),
        max_floor: Optional[float] = Query(None, alais='floor[to]'),
        min_area: Optional[float] = Query(None, alais='area[from]'),
        max_area: Optional[float] = Query(None, alais='area[to]'),
        property_type: Optional[PropertyChoices] = Query(None),
        region: Optional[str] = Query(None),
        city: Optional[str] = Query(None),
        db: Session = Depends(get_db)
):

    query = db.query(Property)
    if min_price is not None:
        query = query.filter(Property.price >= min_price)
    if max_price is not None:
        query = query.filter(Property.price >= max_price)
    if min_floor is not None:
        query = query.filter(Property.floor >= min_floor)
    if max_floor is not None:
        query = query.filter(Property.floor >= max_floor)
    if min_area is not None:
        query = query.filter(Property.area >= min_area)
    if max_area is not None:
        query = query.filter(Property.area >= max_area)
    if property_type is not None:
        query = query.filter(Property.property_type == property_type)
    if region is not None:
        query = query.filter(Property.region == region)
    if city is not None:
        query = query.filter(Property.city == city)


    properties = query.all()

    if not properties:
        raise HTTPException(status_code=404, detail='Property not found')
    return  properties


@property_router.get('/{car.id}/', response_model=List[PropertyOutSchema])
async def property_detail(property_id: int, db: Session = Depends(get_db)):
    property_db = db.query(Property).filter(Property.id == property_id).first()
    if not property_db:
        raise HTTPException(status_code=404, detail='Property not found')
    return [property_db]


@property_router.put('/', response_model=PropertyOutSchema)
async def property_update(property_id: int, property: PropertyCreateSchema,
                          db: Session = Depends(get_db)):
    property_db = db.query(Property).filter(Property.id == property_id).first()
    if not property_db:
        raise HTTPException(status_code=404, detail='Properties updates')

    for property_key, property_value, in property.dict().items():
        setattr(property_db, property_key, property_value)

    db.add(property_db)
    db.commit()
    db.refresh(property_db)
    return property_db


@property_router.delete('/{property_id}/')
async def property_delete(property_id: int, db: Session = Depends(get_db)):
    property_db = db.query(Property).filter(Property.id == property_id).firat()
    if property_db is None:
        raise HTTPException(status_code=404, detail='Property not found')

    db.add(property_db)
    db.commit()
    return {'message': 'Deleted'}