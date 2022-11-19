from fastapi import APIRouter, Depends
from pydantic import BaseModel
from queries.user_queries import UsersList, UserQueries, UserIn, UserOut

router = APIRouter()

@router.get("/users", response_model=UsersList)
def users_list(queries: UserQueries = Depends()):
    return {
        "users": queries.get_all_users(),
    }
@router.get("/users/{user_id}", response_model=UserOut)
def get_user_by_id(user_id: int, queries: UserQueries = Depends()):
    return queries.get_one_user(user_id)

@router.post('/users', response_model=UserOut)
def post_user(user:UserIn, queries:UserQueries = Depends()):
    return queries.post_user(user)

@router.delete("/user/{user_id}", response_model=bool)
def delete_user(user_id: int, queries: UserQueries = Depends()):
    return queries.delete_user(user_id)

@router.put("/users/{user_id}", response_model=UserOut)
def update_user(
    user_id: int, user: UserIn, queries: UserQueries = Depends()
):
    return queries.update_user(user_id, user)
