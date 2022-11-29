from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8001",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/launch-details")
def launch_details():
    return {
        "launch_details": {
            "year": 2022,
            "month": 12,
            "day": "9",
            "hour": 19,
            "min": 0,
            "tz:": "PST",
        }
    }
