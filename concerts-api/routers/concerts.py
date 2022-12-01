from fastapi import APIRouter, Depends
from pydantic import BaseModel, HttpUrl
from datetime import date
from queries.concert_queries import (
    ConcertIn,
    ConcertOut,
    ConcertsList,
    ConcertQueries,
)
from typing import Union
import requests
import json
import os
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

# from jose import jwt, JWTError


router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
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
    user = ConcertOut(**payload.get("account"))
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
    user_id: int, queries: ConcertQueries = Depends(get_current_user)
):
    return {"concerts": queries.get_all(user_id)}


# get one favorite concert for a specific user
@router.get(
    "/concerts/favorites/{user_id}/{concert_id}", response_model=ConcertOut
)
def get_favorite_concert_by_id(
    concert_id: int,
    user_id: int,
    queries: ConcertQueries = Depends(get_current_user),
):
    return queries.get_one(concert_id, user_id)


@router.put(
    "/concerts/favorites/{user_id}/{concert_id}", response_model=ConcertOut
)
def update_favorite_concert(
    concert_id: int,
    concert: ConcertIn,
    queries: ConcertQueries = Depends(get_current_user),
):
    return queries.update(concert_id, concert)


@router.delete(
    "/concerts/favorites/{user_id}/{concert_id}", response_model=bool
)
def delete_concert(
    concert_id: int, queries: ConcertQueries = Depends(get_current_user)
):
    return queries.delete(concert_id)


@router.get("/concerts/{lat},{long}")
def get_all_concerts(lat, long):

    key = os.environ.get("TICKETMASTER_API_KEY")

    url = f"https://app.ticketmaster.com/discovery/v2/events/?apikey={key}&latlong={lat},{long}&locale=*&startDateTime=2022-11-28T17:58:00Z&sort=date,asc&classificationName=music"

    response = requests.get(url)
    data = json.loads(response.content)

    events = data["_embedded"]["events"]
    concerts = []
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
            concert["venue"] = "no venue"

        concert["date"] = event["dates"]["start"]["localDate"]
        try:
            concert["spotify_url"] = event["_embedded"]["attractions"][0][
                "externalLinks"
            ]["spotify"][0]["url"]
        except KeyError:
            continue
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
