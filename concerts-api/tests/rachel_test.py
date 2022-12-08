from main import app
from fastapi.testclient import TestClient
from queries.concert_queries import ConcertQueries
from routers import concerts

client = TestClient(app)


async def override_get_fake_user():
    return {
        "id": 1,
        "first_name": "rachel",
        "last_name": "johnson",
        "email": "rachel@gmail.com",
        "username": "rachel",
    }


test_concert_list_by_user = [
    {
        "id": 1,
        "concert_name": "ooga",
        "artist_name": "booga",
        "start_date": "2022-12-08",
        "min_price": 30,
        "max_price": 35,
        "user_id": 1,
        "spotify_url": "spotify.com",
        "image_url": "image.com",
        "favorite": True,
    }
]


class EmptyConcertQueries:
    def get_all(self, user_id: int):
        return test_concert_list_by_user


def test_not_authorized_user():
    response = client.get("/concerts/favorites/1")
    assert response.status_code == 401


def test_concerts_by_user_id():
    app.dependency_overrides[
        concerts.get_current_user
    ] = override_get_fake_user
    app.dependency_overrides[ConcertQueries] = EmptyConcertQueries
    response = client.get("/concerts/favorites/1")
    assert {"concerts": test_concert_list_by_user} == response.json()
