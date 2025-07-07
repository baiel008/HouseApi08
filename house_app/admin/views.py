from house_app.db.models import UserProfile, RefreshToken, Review, Property
from sqladmin import ModelView

class UserProfileAdmin(ModelView, model=UserProfile):
    column_list = [UserProfile.first_name, UserProfile.last_name, UserProfile.username,
                   UserProfile.email, UserProfile.age, UserProfile.password, UserProfile.role,
                   UserProfile.phone_number]


class RefreshAdmin(ModelView, model=RefreshToken):
    column_list = [RefreshToken.id, RefreshToken.token, RefreshToken.created_date]


class PropertyAdmin(ModelView, model=Property):
    column_list = [Property.title, Property.property_type,
                   Property.description, Property.region,
                   Property.city, Property.district, Property.address,
                   Property.area, Property.price, Property.floor,
                   Property.total_floors, Property.condition, Property.images]


class ReviewAdmin(ModelView, model=Review):
    column_list = [Review.id, Review.seller,
                   Review.buyer, Review.rating,
                   Review.comment]