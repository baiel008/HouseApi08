from fastapi import APIRouter
from house_app.db.database import SessionLocal
from sqlalchemy.orm import Session
from typing import List, Optional
from starlette.requests import Request
from authlib.integrations.starlette_client import OAuth
from house_app.config import settings



social_router = APIRouter(prefix='/oauth', tags=['Social Pauth'])
oauth = OAuth()

oauth.register(
    name = 'google',
    client_id = settings.GOOGLE_CLIENT_ID,
    secret_key = settings.GOOGLE_SECRET,
    authorize_url="https://accounts.google.com/o/oauth2/auth",
    client_kwargs={"scope": "openid profile email"},
)

@social_router.get('/google')
async def login_google(request: Request):
    redirect_uri = settings.GOOGLE_URL
    return await oauth.google.authorize_redirect(request, redirect_uri)