from fastapi import APIRouter, Depends
from pydantic import BaseModel
from datetime import date
from queries.concert_queries import ConcertIn, ConcertOut, ConcertsList, ConcertQueries
import requests
import json

router = APIRouter()

#when we create a concert
@router.get('/concerts/favorites', response_model=ConcertsList)
def get_favorite_concerts(queries:ConcertQueries = Depends()):
    return {"concerts": queries.get_all()}


@router.get("/concerts/favorites/{concert_id}", response_model=ConcertOut)
def get_favorite_concert_by_id(concert_id: int, queries: ConcertQueries = Depends()):
    return queries.get_one(concert_id)

@router.post("/concerts/favorites", response_model=ConcertOut)
def post_favorite_concert(concert:ConcertIn, queries:ConcertQueries = Depends()):
    return queries.create(concert)


@router.put("/concerts/favorites/{concert_id}", response_model=ConcertOut)
def update_favorite_concert(
    concert_id: int, concert: ConcertIn, queries: ConcertQueries = Depends()
):
    return queries.update(concert_id, concert)


@router.delete("/concerts/favorites/{concert_id}", response_model=bool)
def delete_concert(concert_id: int, queries: ConcertQueries = Depends()):
    return queries.delete(concert_id)



url = "https://app.ticketmaster.com/discovery/v2/events"

params = {"classificationName":"music",
          "dmaId": "324",
          "apikey": "cWcKvvPCgHDAZ3eGfT96AeQec01G8wsM" }

response = requests.get(url, params=params)
content = json.loads(response.content)

async def get_ticketmaster_concerts():
  response = requests.get(url, params=params)
  content = json.loads(response.content)
  return content

@router.get("/concerts")
def get_all_concerts(data: get_ticket_master_concerts = Depends()):
    events = content['_embedded']['events']
    concerts=[]
    for event in events:
        concert = {}
        concert["concert_name"]= event['name']
        concert["artist_name"] = event['_embedded']['attractions'][0]['name']
        concert["venue"] = event['_embedded']['venues'][0]['name']
        concert["date"] = event['dates']['start']['localDate']
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
