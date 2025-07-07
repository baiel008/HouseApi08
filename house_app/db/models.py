from house_app.db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import (
    String, Integer, DateTime, Enum, ForeignKey,
    DECIMAL, Text
)
from typing import Optional, List
from datetime import datetime
from enum import Enum as PyEnum


class StatusChoices(str, PyEnum):
    seller = 'seller'
    buyer = 'buyer'


class PropertyChoices(str, PyEnum):
    Elite = 'Elite'
    seria_105 = 'seria_105'
    seria_106 = 'seria_106'
    seria_104 = 'seria_104'
    individual_project = 'individual_project'


class UserProfile(Base):
    __tablename__ = 'user_profile'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(65))
    last_name: Mapped[str] = mapped_column(String(34))
    age: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    username: Mapped[str] = mapped_column(String(32))
    email: Mapped[str] = mapped_column(String(32), unique=True)
    password: Mapped[str] = mapped_column(String, nullable=False)
    role: Mapped[StatusChoices] = mapped_column(Enum(StatusChoices), default=StatusChoices.buyer)
    phone_number: Mapped[Optional[str]] = mapped_column(String(12), nullable=True)
    sellers: Mapped[List['Property']] = relationship('Property', back_populates='seller',
                                                     cascade='all, delete-orphan')
    review_given: Mapped[List['Review']] = relationship('Review', back_populates='buyer',
                                                             foreign_keys="Review.buyer_id",
                                                             cascade='all, delete-orphan')
    review_received: Mapped[List['Review']] = relationship('Review', back_populates='seller',
                                                                foreign_keys="Review.seller_id",
                                                                cascade='all, delete-orphan')
    user_token: Mapped[List['RefreshToken']] = relationship('RefreshToken', back_populates='user',
                                                            cascade='all, delete-orphan')


class RefreshToken(Base):
    __tablename__ = 'refresh_token'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user_profile.id'))
    user: Mapped[UserProfile] = relationship(UserProfile, back_populates='user_token')
    token: Mapped[str] = mapped_column(String, nullable=False)
    created_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)





class Property(Base):
    __tablename__ = 'property'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(64))
    property_type: Mapped[PropertyChoices] = mapped_column(Enum(PropertyChoices), default=PropertyChoices.Elite)
    description: Mapped[str] = mapped_column(String(500))
    region: Mapped[str] = mapped_column(String(64))
    city: Mapped[str] = mapped_column(String(65))
    district: Mapped[str] = mapped_column(String(64))
    address: Mapped[str] = mapped_column(String(64))
    area: Mapped[int] = mapped_column(Integer)
    price: Mapped[int] = mapped_column(DECIMAL(10, 2))
    floor: Mapped[int] = mapped_column(Integer)
    total_floors: Mapped[int] = mapped_column(Integer)
    condition: Mapped[str] = mapped_column(String(165))
    images: Mapped[str] = mapped_column(String(64))
    seller_id: Mapped[int] = mapped_column(ForeignKey('user_profile.id'), nullable=False)
    seller: Mapped['UserProfile'] = relationship('UserProfile', back_populates='sellers')




class Review(Base):
    __tablename__ = 'review'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    seller_id: Mapped[int] = mapped_column(ForeignKey('user_profile.id'), nullable=False)
    seller: Mapped['UserProfile'] = relationship('UserProfile', back_populates='review_received',
                                                 foreign_keys=[seller_id])

    buyer_id: Mapped[int] = mapped_column(ForeignKey('user_profile.id'), nullable=False)
    buyer: Mapped['UserProfile'] = relationship('UserProfile', back_populates='review_given',
                                                foreign_keys=[buyer_id])
    rating: Mapped[int] = mapped_column(Integer)
    comment: Mapped[str] = mapped_column(Text)
