from pydantic import BaseModel
import os
from psycopg_pool import ConnectionPool


class UserIn(BaseModel):
    first_name: str
    last_name: str
    email: str
    username: str

class UserOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    username: str

class UsersList(BaseModel):
    users: list[UserOut]

pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"])

class UserQueries:
    def get_all_users(self):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT id, first_name, last_name, email, username
                    FROM user_info
                    ORDER BY last_name, first_name
                    """
                )

                results = []
                for row in cur.fetchall():
                    record = {}
                    for i, column in enumerate(cur.description):
                        record[column.name] = row [i]
                    results.append(record)

                return results

    def get_one_user(self, user_id: int) -> UserOut:
        with pool.connection() as conn:
            with conn.cursor() as cur:
                result = cur.execute(
                    """
                    SELECT u.id, u.first_name, u.last_name, u.email, u.username
                    FROM user_info AS u
                    WHERE u.id = %s
                    """,
                    [user_id],
                )

                record = result.fetchone()
                print(record)
                data = {
                    "id": record[0],
                    "first_name": record[1],
                    "last_name": record[2],
                    "email": record[3],
                    "username": record[4],
                }
            return UserOut(**data)

    def post_user(self, user: UserIn) -> UserOut:
        with pool.connection() as conn:
            with conn.cursor() as cur:
                result = cur.execute(
                    """
                    INSERT INTO user_info
                        (first_name, last_name, email, username)
                    VALUES
                        (%s, %s, %s, %s)
                    RETURNING id;
                    """,
                    [
                        user.first_name,
                        user.last_name,
                        user.email,
                        user.username,
                    ],
                )

                id = result.fetchone()[0]
                print(id)
                old_data = user.dict()
                print(old_data)
                return UserOut(id=id, **old_data)
    def delete_user(self, user_id: int):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    DELETE FROM user_info
                    WHERE id = %s
                    """,
                    [user_id],
                )
                return True

    def update_user(self, user_id, user: UserIn) -> UserOut:
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    UPDATE user_info
                    SET
                    first_name = %s,
                    last_name = %s,
                    email = %s,
                    username = %s


                    """,
                    [
                        user.first_name,
                        user.last_name,
                        user.email,
                        user.username,
                    ],
                )

                old_data = user.dict()
                print(old_data)
                return UserOut(id=user_id, **old_data)
