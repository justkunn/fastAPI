from fastapi import FastAPI
from routes import usersAPI
# from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="portal's data users", summary="endpoint data", version="1.0")


app.include_router(router=usersAPI)