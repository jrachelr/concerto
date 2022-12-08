from main import app
from fastapi.testclient import TestClient
from queries.user_queries import UserQueries, UserOut
from authenticator import authenticator

client = TestClient(app)

def test_get_current_user():
    account = {
        "id": 5,
        "first_name": "string",
        "last_name": "string",
        "email": "string",
        "username": "string"
    }

    app.dependency_overrides[
        authenticator.try_get_current_account_data
    ] = lambda: account

    response = client.get("/users/current")
    app.dependency_overrides = {}
    assert response.status_code == 200
    data = response.json()
    assert data == account
