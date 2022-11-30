from fastapi import FastAPI, APIRouter, Depends
from pydantic import BaseModel, HttpUrl
from typing import Union
from routers import concerts
import requests
import json
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        os.environ.get(
            "CORS_HOST",
            "REACT_APP_ACCOUNTS_HOST",
        ), "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(concerts.router)

invoices_callback_router = APIRouter()

# url = "https://app.ticketmaster.com/discovery/v2/events/?apikey={key}&latlong={lat},{long}&locale=*&startDateTime=2022-11-28T17:58:00Z&sort=date,asc&classificationName=music"

# # # params = {"classificationName":"music",
# # #           "latlong": "34.0522342,-118.2436849",
# # #           "sort": "date,asc",
# # #           "locale": "*",
# # #           "startDateTime": "2022-11-21T16:10:00Z",
# # #           "apikey": "cWcKvvPCgHDAZ3eGfT96AeQec01G8wsM" }


# async def get_ticketmaster_concerts():
#   response = requests.get(url)
#   content = json.loads(response.content)
#   return content

# # class ConcertLocation(BaseModel):
# #     lat: str
# #     long: str

# # class ConcertReceived(BaseModel):
# #     ok: bool

# # callback_url = 'https://app.ticketmaster.com/discovery/v2/events'




# # @invoices_callback_router.get(
# #     "https://app.ticketmaster.com/discovery/v2/events/?apikey={key}&latlong={$request.body.lat},{$request.body.long}&locale=*&startDateTime=2022-11-28T17:58:00Z&sort=date,asc&classificationName=music", response_model=ConcertReceived
# # )
# # def get_concerts():
# #     pass

# # @app.post("/concerts", callbacks=invoices_callback_router.routes)
# # def create_concert(concert: ConcertLocation, callback_url: Union[HttpUrl, None] = None):
# #     pass


@app.get("/concerts/{lat},{long}")
def get_all_concerts(lat, long):

    key = os.environ.get("TICKETMASTER_API_KEY")

    url = f"https://app.ticketmaster.com/discovery/v2/events/?apikey={key}&latlong={lat},{long}&locale=*&startDateTime=2022-11-28T17:58:00Z&sort=date,asc&classificationName=music"

    response = requests.get(url)
    data = json.loads(response.content)

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
