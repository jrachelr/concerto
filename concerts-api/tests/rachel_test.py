from main import app
from fastapi.testclient import TestClient
from queries.concert_queries import ConcertQueries
from fastapi.security import OAuth2

client = TestClient(app)

reusable_oauth2 = OAuth2(
    flows={
        "password": {
            "tokenUrl": "token",
            "scopes": {},
        }
    }
)

test_concert = {
    "id": 1,
    "concert_name": str,
    "artist_name": str,
    "user_id": int,
}

test_user = {
    "id": int,
    "first_name": str,
    "last_name": str,
    "email": str,
    "username": str,
}


class EmptyConcertQueries:
    def get_concerts_by_user(self, user_id: int):
        return []


async def override_dependency(reusable_oauth2):
    return {}


def test_concerts_by_user():
    app.dependency_overrides[ConcertQueries] = EmptyConcertQueries

    response = client.get("/concerts/favorites/1")

    app.dependency_overrides = override_dependency

    assert response.status_code == 200
    assert response.json() == {"concerts": []}
