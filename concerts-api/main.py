from fastapi import FastAPI, APIRouter, Depends
from pydantic import BaseModel, HttpUrl
from typing import Union
from routers import concerts
import requests
import json
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        os.environ.get(
            "CORS_HOST",
            "REACT_APP_ACCOUNTS_HOST",
        ), "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(concerts.router)
