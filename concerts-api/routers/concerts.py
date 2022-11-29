from fastapi import APIRouter, Depends
from pydantic import BaseModel, HttpUrl
from datetime import date
from queries.concert_queries import ConcertIn, ConcertOut, ConcertsList, ConcertQueries
from typing import Union
import requests
import json

router = APIRouter()


#add favorite concert
@router.post("/concerts/favorites/{user_id}", response_model=ConcertOut)
def post_favorite_concert(concert:ConcertIn, user_id: int, queries:ConcertQueries = Depends()):
    return queries.create(concert, user_id)

#get favorite concerts for all users
@router.get('/concerts/favorites/', response_model=ConcertsList)
def get_favorite_concerts(queries:ConcertQueries = Depends()):
    return {"concerts": queries.get_all()}

#get favorite concerts for a specific user
@router.get('/concerts/favorites/{user_id}', response_model=ConcertsList)
def get_favorite_concerts(user_id: int, queries:ConcertQueries = Depends()):
    return {"concerts": queries.get_all(user_id)}

#get one favorite concert for a specific user
@router.get("/concerts/favorites/{user_id}/{concert_id}", response_model=ConcertOut)
def get_favorite_concert_by_id(concert_id: int, user_id: int, queries: ConcertQueries = Depends()):
    return queries.get_one(concert_id, user_id)

@router.put("/concerts/favorites/{user_id}/{concert_id}", response_model=ConcertOut)
def update_favorite_concert(
    concert_id: int, concert: ConcertIn, queries: ConcertQueries = Depends()
):
    return queries.update(concert_id, concert)

@router.delete("/concerts/favorites/{user_id}/{concert_id}", response_model=bool)
def delete_concert(concert_id: int, queries: ConcertQueries = Depends()):
    return queries.delete(concert_id)
