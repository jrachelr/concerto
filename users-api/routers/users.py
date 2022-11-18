from fastapi import APIRouter, Depends
from pydantic import BaseModel
from queries.user_queries import UserOut, UsersOut, UserQueries

router = APIRouter()

@router.get("/users", response_model=UsersOut)
def users_list(queries: UserQueries = Depends()):
    return {
        "users": queries.get_all_users(),
    }
