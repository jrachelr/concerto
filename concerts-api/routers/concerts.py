from fastapi import APIRouter, Depends
from pydantic import BaseModel
from datetime import date
from queries.concert_queries import ConcertIn, ConcertOut, ConcertsList, ConcertQueries
import requests
import json

router = APIRouter()

#when we create a concert
@router.get('/concerts/favorites', response_model=ConcertsList)
def get_all_concerts(queries:ConcertQueries = Depends()):
    return {"concerts": queries.get_all_favorites()}

@router.get('/concerts/{concert_id}', response_model=ConcertOut)
def get_concert_by_id(concert_id:int, queries:ConcertQueries = Depends()):
    return queries.get_one_concert(concert_id)

@router.post('/concerts/favorites', response_model=ConcertOut)
def post_concert(concert:ConcertIn, queries:ConcertQueries = Depends()):
    return queries.add_favorite_concert(concert)
