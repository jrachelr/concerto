# from fastapi import APIRouter, Depends
# from pydantic import BaseModel
# from datetime import date
# from queries import ConcertQueries

# router = APIRouter()

# class ConcertIn(BaseModel):

#     name: str
#     artist: str
#     dates: date
#     min_price: int
#     max_price: int

# class ConcertOut(BaseModel):
#     id: int
#     name: str
#     artist: str
#     dates: date
#     min_price: int
#     max_price: int


# class ConcertsList(BaseModel):
#     concerts: list(ConcertOut)

# @router.get('/concerts/{id}', response_model=ConcertOut):
# def get_concert_by_id(
#     concert_id: int,
#     queries: ConcertQueries = Depends()
# ):
#     pass


# @router.get('/concerts', response_model=ConcertsOut)
# def get_concerts(queries: ConcertQueries = Depends()):
#     concerts = queries.get_all_concerts()
#     return {'concerts': concerts}
