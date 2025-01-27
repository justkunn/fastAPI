from fastapi import APIRouter
from routes.tokenRoutes import tokenRoute
from .userRoutes import userRoute

usersAPI = APIRouter()

usersAPI.include_router(router=userRoute, tags=["User Routes"])
usersAPI.include_router(router=tokenRoute, tags=["Token Routes"])