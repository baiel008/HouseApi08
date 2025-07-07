from fastapi import HTTPException, Depends, APIRouter
from house_app.db.models import Review
from house_app.db.schema import ReviewCreateSchema, ReviewSchema
from house_app.db.database import SessionLocal
from sqlalchemy.orm import Session
from typing import List



async def get_db():
    db = SessionLocal()
    try:
        yield  db
    finally:
        db.close()


review_router = APIRouter(prefix='/review', tags=['Review'])


@review_router.post('/', response_model=dict)
async def rating_create(rating: ReviewCreateSchema, db: Session = Depends(get_db)):
    rating_db = Review(**rating.dict())
    db.add(rating_db)
    db.commit()
    db.refresh(rating_db)
    return {'message': 'Saved'}


@review_router.delete('/{review_id}/')
async def rating_delete(review_id: int, db: Session = Depends(get_db)):
    review_db = db.query(Review).filter(Review.id == review_id).first()
    if review_db is None:
        raise HTTPException(status_code=404, detail='Review not found')

    db.delete(review_db)
    db.commit()
    return {'message': 'Deleted'}
