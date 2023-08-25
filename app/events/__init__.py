from fastapi import APIRouter
from app.events.views import router

API_STR = "/api"

events_router = APIRouter(prefix=API_STR)
events_router.include_router(router)
