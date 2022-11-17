import os
from psycopg_pool import ConnectionPool
from datetime import date
from pydantic import BaseModel

class ConcertIn(BaseModel):
    concert_name: str
    artist_name: str
    start_date: date
    min_price: int
    max_price: int

class ConcertOut(BaseModel):
    id: int
    concert_name: str
    artist_name: str
    start_date: date
    min_price: int
    max_price: int


class ConcertsList(BaseModel):
    concerts: list[ConcertOut]

pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"])


#need to fix so it can return the id as well
class ConcertQueries:
    def add_favorite_concert(self, concert:ConcertIn) -> ConcertOut:
        with pool.connection() as conn:
            with conn.cursor() as cur:
                result = cur.execute(
                    """
                    INSERT INTO concert_info
                        (concert_name, artist_name, start_date, min_price, max_price)
                    VALUES
                        (%s, %s, %s, %s, %s)
                    RETURNING id;
                    """,
                    [concert.concert_name, concert.artist_name, concert.start_date, concert.min_price, concert.max_price]
                )

                id = result.fetchone()[0]
                print(id)
                old_data = concert.dict()
                print(old_data)
                return ConcertOut(id = id, **old_data)
    def get_all_favorites(self) -> ConcertOut:
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT *
                    FROM concert_info
                    ORDER BY concert_name
                    """,
                )

                results = []
                for row in cur.fetchall():
                    concert = {}
                    for i, column in enumerate(cur.description):
                        concert[column.name] = row[i]
                    results.append(concert)

                return results

    def get_one_concert(self, concert_id:int) -> ConcertOut:
        with pool.connection() as conn:
            with conn.cursor() as cur:
                result = cur.execute(
                    """
                    SELECT c.id, c.concert_name, c.artist_name, c.start_date, c.min_price, c.max_price
                    FROM concert_info AS c
                    WHERE c.id = %s
                    """,
                    [concert_id],
                )

                record = result.fetchone()
                print(record)
                data = {
                    "id": record[0],
                    "concert_name": record[1],
                    "artist_name": record[2],
                    "start_date": record[3],
                    "min_price": record[4],
                    "max_price": record[5],
                }
            return ConcertOut(**data)
