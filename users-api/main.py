from fastapi import FastAPI
from routers import users
from authenticator import authenticator

app = FastAPI()


app.include_router(users.router)
app.include_router(authenticator.router)
