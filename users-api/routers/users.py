from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from pydantic import BaseModel
from jwtdown_fastapi.authentication import Token
from authenticator import authenticator
from queries.user_queries import UsersList, UserQueries, UserIn, UserOut

router = APIRouter()



class AccountForm(BaseModel):
    username: str
    password: str

class AccountToken(Token):
    account: UserOut

class HttpError(BaseModel):
    detail: str

router = APIRouter()


@router.post("/users", response_model=AccountToken | HttpError)
async def post_user(
    info: UserIn,
    request: Request,
    response: Response,
    repo: UserQueries = Depends(),
):
    hashed_password = authenticator.hash_password(info.password)
    account = repo.create_user(info, hashed_password)
    form = AccountForm(username=info.email, password=info.password)
    token = await authenticator.login(response, request, form, repo)
    return AccountToken(account=account, **token.dict())



@router.get("/users", response_model=UsersList)
def users_list(queries: UserQueries = Depends()):
    return {
        "users": queries.get_all_users(),
    }

@router.get("/users/current", response_model=UserOut)
def get_user_by_info(account: UserOut = Depends(authenticator.get_current_account_data)):
    return account

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
