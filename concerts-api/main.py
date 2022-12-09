from fastapi import FastAPI
from routers import concerts
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        os.environ.get(
            "CORS_HOST",
            "USERS_API_HOST",
        ), "http://localhost:3000",
        "https://the-jerney.gitlab.io/",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(concerts.router)
