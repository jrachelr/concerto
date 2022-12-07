import os
#from psycopg_pool import ConnectionPool
from datetime import date
from psycopg import connect
from pydantic import BaseModel

keepalive_kwargs = {
   "keepalives": 1,
   "keepalives_idle": 60,
   "keepalives_interval": 10,
   "keepalives_count": 5
  }

class Concert(BaseModel):
    id: int
    concert_name: str
    artist_name: str
    start_date: date
    min_price: int
    max_price: int
    user_id: int
    spotify_url: str
    image_url: str
    favorite: bool

class ConcertIn(BaseModel):
    concert_name: str
    artist_name: str
    start_date: date
    min_price: int
    max_price: int
    spotify_url: str
    image_url: str
    favorite: bool


class ConcertOut(BaseModel):
    id: int
    concert_name: str
    artist_name: str
    start_date: date
    min_price: int
    max_price: int
    user_id: int
    spotify_url: str
    image_url: str
    favorite: bool

class UserOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    username: str


class ConcertsList(BaseModel):
    concerts: list[ConcertOut]


#pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"])
conn = connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs)


# need to fix so it can return the id as well
class ConcertQueries:
    def create(self, concert: ConcertIn, user_id: int) -> ConcertOut:
        #with pool.connection() as conn:
            with conn.cursor() as cur:
                result = cur.execute(
                    """
                    INSERT INTO favorite_concerts
                        (concert_name, artist_name, start_date, min_price, max_price, user_id, spotify_url, image_url, favorite)
                    VALUES
                        (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    RETURNING id;
                    """,
                    [
                        concert.concert_name,
                        concert.artist_name,
                        concert.start_date,
                        concert.min_price,
                        concert.max_price,
                        user_id,
                        concert.spotify_url,
                        concert.image_url,
                        concert.favorite
                    ],
                )

                id = result.fetchone()[0]
                old_data = concert.dict()
                return ConcertOut(id=id, user_id=user_id, **old_data)

    def get_all(self, user_id:int=None) -> list[ConcertOut]:
        #with pool.connection() as conn:
            with conn.cursor() as cur:
                if user_id == None:
                    cur.execute(
                        """
                        SELECT *
                        FROM favorite_concerts
                        """
                    )
                else:
                    cur.execute(
                        """
                        SELECT *
                        FROM favorite_concerts
                        WHERE user_id = %s
                        """,
                        [user_id]
                    )

                results = []
                for row in cur.fetchall():
                    concert = {}
                    for i, column in enumerate(cur.description):
                        concert[column.name] = row[i]
                    results.append(concert)

                return results

    def get_one(self, concert_id: int, user_id: int) -> ConcertOut:
        #with pool.connection() as conn:
            with conn.cursor() as cur:
                result = cur.execute(
                    """
                    SELECT *
                    FROM favorite_concerts AS f
                    WHERE f.id = %s AND f.user_id = %s
                    """,
                    [concert_id, user_id]
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
                    "user_id": record[6],
                    "spotify_url": record[7],
                    "image_url": record[8],
                    "favorite": record[9]
                }
            return ConcertOut(**data)

    def update(self, user_id, concert_id, concert: ConcertIn) -> ConcertOut:
        #with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    UPDATE favorite_concerts
                    SET
                    concert_name = %s,
                    artist_name = %s,
                    start_date = %s,
                    min_price = %s,
                    max_price = %s,
                    spotify_url = %s,
                    image_url = %s,
                    favorite = %s

                    WHERE user_id = %s AND id = %s


                    """,
                    [
                        concert.concert_name,
                        concert.artist_name,
                        concert.start_date,
                        concert.min_price,
                        concert.max_price,
                        concert.spotify_url,
                        concert.image_url,
                        concert.favorite,
                        user_id,
                        concert_id

                    ],
                )

                old_data = concert.dict()
                print(old_data)
                return ConcertOut(id=concert_id, user_id = user_id, **old_data)

    def delete(self, user_id: int, concert_id: int):
        #with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    DELETE FROM favorite_concerts
                    WHERE id = %s AND user_id = %s
                    """,
                    [concert_id, user_id],
                )
                return True
