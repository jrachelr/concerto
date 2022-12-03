from fastapi import APIRouter, Depends
from pydantic import BaseModel
from datetime import date
from queries.concert_queries import (
    ConcertIn,
    ConcertOut,
    ConcertsList,
    ConcertQueries,
    UserOut,
)
import requests
import json
import os
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

# from jose import jwt, JWTError


router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="localhost:8001/token")
print("test outhhhhhhhhh", oauth2_scheme)
SECRET_KEY = os.environ.get("SIGNING_KEY", "blah")
print("test striiiiing", SECRET_KEY)


async def get_current_user(token: str = Depends(oauth2_scheme)):
    print("fjdsakfldjsflkjlk")
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY)
        print("tesitngggggggg")
        username: str = payload.get("sub")
        if username is None:
            print("niceeeeeee")
            raise credentials_exception

    except JWTError:
        raise credentials_exception
        print("another one")
    user = UserOut(**payload.get("account"))
    if user is None:
        print("yesssssss")
        raise credentials_exception
    return user


not_authorized = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid authentication credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


# add favorite concert
@router.post("/concerts/favorites/{user_id}", response_model=ConcertOut)
def post_favorite_concert(
    concert: ConcertIn,
    user_id: int,
    queries: ConcertQueries = Depends(),
    account: dict = Depends(get_current_user),
):
    if account:
        return queries.create(concert, user_id)


# get favorite concerts for all users
@router.get("/concerts/favorites/", response_model=ConcertsList)
def get_favorite_concerts(
    queries: ConcertQueries = Depends(),
    account: dict = Depends(get_current_user),
):
    print("THISISSSSSS SIS SITTTTTTT", account)
    if account:
        return {"concerts": queries.get_all()}


# get favorite concerts for a specific user
@router.get("/concerts/favorites/{user_id}", response_model=ConcertsList)
def get_favorite_concerts_by_id(
    user_id: int,
    queries: ConcertQueries = Depends(),
    account: dict = Depends(get_current_user),
):
    if account:
        return {"concerts": queries.get_all(user_id)}


# get one favorite concert for a specific user
@router.get(
    "/concerts/favorites/{user_id}/{concert_id}", response_model=ConcertOut
)
def get_favorite_concert_by_id(
    concert_id: int,
    user_id: int,
    queries: ConcertQueries = Depends(),
    account: dict = Depends(get_current_user),
):
    if account:
        return queries.get_one(concert_id, user_id)


@router.put(
    "/concerts/favorites/{user_id}/{concert_id}", response_model=ConcertOut
)
def update_favorite_concert(
    user_id: int,
    concert_id: int,
    concert: ConcertIn,
    queries: ConcertQueries = Depends(),
    account: dict = Depends(get_current_user),
):
    if account:
        return queries.update(user_id, concert_id, concert)


@router.delete(
    "/concerts/favorites/{user_id}/{concert_id}", response_model=bool
)
def delete_concert(
    user_id: int,
    concert_id: int,
    queries: ConcertQueries = Depends(),
    account: dict = Depends(get_current_user),
):
    if account:
        return queries.delete(user_id, concert_id)


url = "https://app.ticketmaster.com/discovery/v2/events"

params = {
    "classificationName": "music",
    "dmaId": "324",
    "apikey": "cWcKvvPCgHDAZ3eGfT96AeQec01G8wsM",
}

response = requests.get(url, params=params)
content = json.loads(response.content)

# get concerts from ticketmaster
async def get_ticketmaster_concerts():
    response = requests.get(url, params=params)
    content = json.loads(response.content)
    return content


@router.get("/concerts")
def get_all_concerts(data: get_ticketmaster_concerts = Depends()):
    events = content["_embedded"]["events"]
    concerts = []
    for event in events:
        concert = {}
        concert["concert_name"] = event["name"]
        concert["artist_name"] = event["_embedded"]["attractions"][0]["name"]
        concert["venue"] = event["_embedded"]["venues"][0]["name"]
        concert["date"] = event["dates"]["start"]["localDate"]
        try:
            concert["min_price"] = event["priceRanges"][0]["min"]
        except KeyError:
            concert["min_price"] = "no minimum price range available"
        concerts.append(concert)
        try:
            concert["max_price"] = event["priceRanges"][0]["max"]
        except KeyError:
            concert["max_price"] = "no maximum price range available"
        concerts.append(concert)
    return {"concerts": concerts}
