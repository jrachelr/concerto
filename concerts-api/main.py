from fastapi import FastAPI, APIRouter, Depends
from pydantic import BaseModel, HttpUrl
from typing import Union
from routers import concerts
import requests
import json

app = FastAPI()


app.include_router(concerts.router)

invoices_callback_router = APIRouter()

url = "https://app.ticketmaster.com/discovery/v2/events?apikey=cWcKvvPCgHDAZ3eGfT96AeQec01G8wsM&locale=*&page=1&sort=date,asc&city=los%20angeles&classificationName=music"

# # params = {"classificationName":"music",
# #           "latlong": "34.0522342,-118.2436849",
# #           "sort": "date,asc",
# #           "locale": "*",
# #           "startDateTime": "2022-11-21T16:10:00Z",
# #           "apikey": "cWcKvvPCgHDAZ3eGfT96AeQec01G8wsM" }


async def get_ticketmaster_concerts():
  response = requests.get(url)
  content = json.loads(response.content)
  return content

class ConcertLocation(BaseModel):
    lat: str
    long: str


class ConcertReceived(BaseModel):
    ok: bool

callback_url = 'https://app.ticketmaster.com/discovery/v2/events'


@invoices_callback_router.get(
    "{$callback_url}/?apikey=cWcKvvPCgHDAZ3eGfT96AeQec01G8wsM&latlong={$request.body.lat},{$request.body.long}&locale=*&startDateTime=2022-11-28T17:58:00Z&sort=date,asc&classificationName=music", response_model=ConcertReceived
)
def get_concerts():
    pass

@app.post("/concerts", callbacks=invoices_callback_router.routes)
def create_concert(concert: ConcertLocation, callback_url: Union[HttpUrl, None] = None):
    return {"msg": "Concert received"}


@app.get("/concerts")
def get_all_concerts(data: get_ticketmaster_concerts = Depends()):

    events = data['_embedded']['events']
    concerts=[]
    for event in events:
        concert = {}
        try:
            concert["artist_name"] = event['_embedded']['attractions'][0]['name']
        except KeyError:
            continue
        concert["image_url"]= event["images"][1]["url"]
        concert["concert_name"]= event['name']
        try:
            concert["venue"] = event['_embedded']['venues'][0]['name']
        except:
            concert["venue"] = "no venue"

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
