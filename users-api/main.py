from fastapi import FastAPI
from routers import users
from authenticator import authenticator
from fastapi.middleware.cors import CORSMiddleware
import os


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        os.environ.get(
            "CORS_HOST",
            "REACT_APP_SAMPLE_SERVICE_API_HOST",
        ), "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(users.router)
app.include_router(authenticator.router)
