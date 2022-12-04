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
from jose import jwt, JWTError


router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="localhost:8001/token")
print("test outhhhhhhhhh", oauth2_scheme)
SECRET_KEY = os.environ.get("SIGNING_KEY", "blah")
print("test striiiiing", SECRET_KEY)


async def get_current_user(token: str = Depends(oauth2_scheme)):
    print("current_user")
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception
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


@router.get("/concerts/{city},{state}")
def get_all_concerts(city, state):

    key = os.environ.get("TICKETMASTER_API_KEY")

    url = f"https://app.ticketmaster.com/discovery/v2/events?apikey={key}&locale=*&startDateTime=2022-12-01T14:40:00Z&size=100&sort=date,asc&city={city}&stateCode={state}&classificationName=music"

    print(url)
    response = requests.get(url)
    data = json.loads(response.content)

    events = data["_embedded"]["events"]

    concerts = []
    artists = []

    for event in events:
        concert = {}
        try:
            concert["artist_name"] = event["_embedded"]["attractions"][0][
                "name"
            ]
        except KeyError:
            continue

        concert["image_url"] = event["images"][1]["url"]
        concert["concert_name"] = event["name"]
        try:
            concert["venue"] = event["_embedded"]["venues"][0]["name"]
        except:
            concert["venue"] = "TBD"

        concert["start_date"] = event["dates"]["start"]["localDate"]
        try:
            concert["spotify_url"] = event["_embedded"]["attractions"][0][
                "externalLinks"
            ]["spotify"][0]["url"]
        except KeyError:
            continue
        try:
            concert["min_price"] = event["priceRanges"][0]["min"]
        except KeyError:
            concert["min_price"] = 0

        try:
            concert["max_price"] = event["priceRanges"][0]["max"]
        except KeyError:
            concert["max_price"] = 0

        if concert["artist_name"] not in artists:
            artists.append(concert["artist_name"])
            concerts.append(concert)
        else:
            continue

        concert["favorite"] = False

    return {"concerts": concerts}
