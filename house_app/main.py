from fastapi import FastAPI
from house_app.api import property, auth, review, social_auth, predict
import uvicorn
from starlette.middleware.sessions import SessionMiddleware
from house_app.config import SECRET_KEY
from house_app.admin.setup import setup_admin

house_app = FastAPI()
house_app.include_router(auth.auth_router)
house_app.include_router(social_auth.social_router)
house_app.include_router(property.property_router)
house_app.include_router(review.review_router)
house_app.include_router(predict.predict_router)
house_app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)
setup_admin(house_app)


if __name__ == '__main__':
    uvicorn.run(house_app, host='127.0.0.1', port=2222)