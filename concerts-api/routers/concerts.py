from fastapi import APIRouter, Depends
from pydantic import BaseModel
from datetime import date
from queries.concert_queries import ConcertIn, ConcertOut, ConcertsList, ConcertQueries
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


url = "https://app.ticketmaster.com/discovery/v2/events"

params = {"classificationName":"music",
          "latlong": "34.0522342,-118.2436849",
          "sort": "date,asc",
          "locale": "*",
          "startDateTime": "2022-11-21T16:10:00Z",
          "apikey": "cWcKvvPCgHDAZ3eGfT96AeQec01G8wsM" }

response = requests.get(url, params=params)
content = json.loads(response.content)

#get concerts from ticketmaster
async def get_ticketmaster_concerts():
  response = requests.get(url, params=params)
  content = json.loads(response.content)
  return content

@router.get("/concerts")
def get_all_concerts(data: get_ticketmaster_concerts = Depends()):
    events = content['_embedded']['events']
    concerts=[]
    for event in events:
        concert = {}
        try:
            concert["artist_name"] = event['_embedded']['attractions'][0]['name']
        except KeyError:
            continue

        concert["concert_name"]= event['name']
        concert["venue"] = event['_embedded']['venues'][0]['name']
        concert["date"] = event['dates']['start']['localDate']
        try:
            concert["spotify_url"] = event['_embedded']['attractions'][0]['externalLinks']['spotify'][0]['url']
        except KeyError:
            continue
        try:
            concert["min_price"] = event['priceRanges'][0]['min']
        except KeyError:
            concert["min_price"] = "no minimum price range available"
        concerts.append(concert)
        try:
            concert["max_price"] = event['priceRanges'][0]['max']
        except KeyError:
            concert["max_price"] = "no maximum price range available"
        concerts.append(concert)
    return {"concerts": concerts}
