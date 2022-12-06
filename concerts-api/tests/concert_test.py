from main import app
from fastapi.testclient import TestClient
from queries.user_queries import UserQueries

client = TestClient(app)


test_test_concert = {
            "id": 1,
            "concert_name": "str",
            "artist_name": "str",
            "email": "str",
            "username": "str",

        }


# FAKE DB
class EmptyUserQueries:
    def get_one_user(self, user_id: int):
        return test_test_user
# MOCK QUERY CLASS


# class NormalUserQueries:
    # def get_one_user(self, user_id: int):
    #     return [user_id, {}, True]


def test_get_user_by_id():
    # ARRANGE
    # Use Fake Database
    app.dependency_overrides[UserQueries] = EmptyUserQueries
    # ACT
    # Make the request
    response = client.get("/users/1")
    app.dependency_overrides = {}
    # ASSERT
    # Assert that we got a 200
    assert response.status_code == 200
    assert response.json() == test_test_user

    # CLEAN UP
    # Clean dependencies
