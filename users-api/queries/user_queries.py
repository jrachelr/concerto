from pydantic import BaseModel
import os
from psycopg_pool import ConnectionPool


class UserOut(BaseModel):
    id: int
    first: str
    last: str
    email: str
    username: str

class UsersOut(BaseModel):
    users: list[UserOut]

pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"])

class UserQueries:
    def get_all_users(self):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT id, first, last, email, username
                    FROM users
                    ORDER BY last, first
                    """
                )

                results = []
                for row in cur.fetchall():
                    record = {}
                    for i, column in enumerate(cur.description):
                        record[column.name] = row [i]
                    results.append(record)

                return results
