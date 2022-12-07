from main import app
from fastapi.testclient import TestClient
from queries.concert_queries import ConcertQueries

client = TestClient(app)

test_concert = {
    "id": int,
    "concert_name": str,
    "artist_name": str,
    "user_id": int,
}


class EmptyConcertQueries:
    def get_concerts_by_user(self, user_id: int):
        return []


def test_concerts_by_user():
    app.dependency_overrides[ConcertQueries] = EmptyConcertQueries

    response = client.get("/concerts/favorites/1")

    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() == test_concert
