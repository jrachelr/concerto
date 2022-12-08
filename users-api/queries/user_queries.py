from pydantic import BaseModel
import os
# from psycopg_pool import ConnectionPool
from psycopg import connect

keepalive_kwargs = {
   "keepalives": 1,
   "keepalives_idle": 60,
   "keepalives_interval": 10,
   "keepalives_count": 5
  }


class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    hashed_password: str
    username: str


class UserIn(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    username: str


class UserOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    username: str


class UsersList(BaseModel):
    users: list[UserOut]


# pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"])
conn = connect(conninfo=os.environ["DATABASE_URL"], **keepalive_kwargs)


class UserQueries:
    def get_all_users(self):
        # with pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, first_name,
                last_name,
                email,
                hashed_password,
                username
                FROM user_info
                ORDER BY last_name, first_name
                """
                        )

            results = []
            for row in cur.fetchall():
                record = {}
                for i, column in enumerate(cur.description):
                    record[column.name] = row[i]
                results.append(record)

            return results

    def get_one_user(self, user_id: int) -> User:
        # with pool.connection() as conn:
        with conn.cursor() as cur:
            result = cur.execute(
                """
                SELECT u.id,
                u.first_name,
                u.last_name,
                u.email,
                u.hashed_password,
                u.last_name,
                u.username
                FROM user_info AS u
                WHERE u.id = %s
                """,
                [user_id],
            )

            record = result.fetchone()
            print(record)
            if record is None:
                return None
            return User(
                id=record[0],
                first_name=record[1],
                last_name=record[2],
                email=record[3],
                hashed_password=record[4],
                username=record[5],
            )

    def get_one_user_email(self, email: str) -> User:
        # with pool.connection() as conn:
        with conn.cursor() as cur:
            result = cur.execute(
                """
                SELECT u.id,
                u.first_name,
                u.last_name,
                u.email,
                u.hashed_password,
                u.last_name,
                u.username
                FROM user_info AS u
                WHERE u.email = %s
                """,
                [email],
            )

            record = result.fetchone()
            print(record)
            if record is None:
                return None
            return User(
                id=record[0],
                first_name=record[1],
                last_name=record[2],
                email=record[3],
                hashed_password=record[4],
                username=record[5],
            )

    def create_user(self, user: UserIn, hashed_password: str) -> User:
        # with pool.connection() as conn:
        with conn.cursor() as cur:
            result = cur.execute(
                """
                INSERT INTO user_info
                    (first_name, last_name, email, hashed_password, username)
                VALUES
                    (%s, %s, %s, %s, %s)
                RETURNING id;
                """,
                [
                    user.first_name,
                    user.last_name,
                    user.email,
                    hashed_password,
                    user.username,
                ],
                )

            id = result.fetchone()[0]
            print(id)
            # old_data = user.dict()
            # print(old_data)
            return User(id=id,
                        first_name=user.first_name,
                        last_name=user.last_name,
                        email=user.email,
                        hashed_password=hashed_password,
                        username=user.username,)

    def delete_user(self, user_id: int):
        # with pool.connection() as conn:
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
        # with pool.connection() as conn:
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
