from main import app
from fastapi.testclient import TestClient
from queries.user_queries import UserQueries

client = TestClient(app)

class EmptyUserQueries:
    def get_all_users(self):
        return []


def test_get_all_users():
    app.dependency_overrides[UserQueries] = EmptyUserQueries

    response = client.get("/users")

    app.dependency_overrides= {}

    assert response.status_code == 200
    assert response.json() == {"users": []}
