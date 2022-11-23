from fastapi import FastAPI
from routers import concerts

app = FastAPI()


app.include_router(concerts.router)
