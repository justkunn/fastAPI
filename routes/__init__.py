from fastapi import APIRouter
from .userRoutes import userRoute

usersAPI = APIRouter()

usersAPI.include_router(router=userRoute, tags=["User Routes"])