from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime
from house_app.db.models import StatusChoices, PropertyChoices

class UserProfileSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    password: str
    email: EmailStr
    age: Optional[int]
    role: StatusChoices
    phone_number: str

    class Config:
        from_attributes = True


class UserProfileCreateSchema(BaseModel):
    first_name: str
    last_name: str
    username: str
    password: str
    email: EmailStr
    age: Optional[int]
    role: StatusChoices = StatusChoices.buyer
    phone_number: str

    class Config:
        from_attributes = True


class UserProfileLoginSchema(BaseModel):
    email: str
    password: str

    class Config:
        from_attributes = True


class PropertyOutSchema(BaseModel):
    id: int
    title: str
    property_type: PropertyChoices
    description: str
    region: str
    city: str
    district: str
    address: str
    area: int
    price: float
    floor: int
    total_floors: int
    condition: str
    images: str
    seller_id: int

    class Config:
        from_attributes = True


class PropertyCreateSchema(BaseModel):
    title: str
    property_type: PropertyChoices
    description: str
    region: str
    city: str
    district: str
    address: str
    area: int
    price: float
    floor: int
    total_floors: int
    condition: str
    images: str
    seller_id: int

    class Config:
        from_attributes = True



class ReviewSchema(BaseModel):
    id: int
    seller_id: int
    buyer_id: int
    rating: int
    comment: str

    class Config:
        from_attributes = True


class ReviewCreateSchema(BaseModel):
    seller_id: int
    buyer_id: int
    rating: int
    comment: str

    class Config:
        from_attributes = True


class HousePredictSchema(BaseModel):
    GrLivArea: int
    YearBuilt: int
    GarageCars: int
    TotalBsmtSF: int
    FullBath: int
    OverallQual: int
    Neighborhood: str