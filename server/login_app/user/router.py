from typing import List
from fastapi import APIRouter,Depends,Response, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from login_app import database
from . import schema
from . import services, validator, token
from .models import User
from .oauth2 import get_current_user

router = APIRouter(tags=['Users'], prefix='/user')

@router.post('/login', status_code=status.HTTP_200_OK)
async def login(request: OAuth2PasswordRequestForm = Depends(), database: Session = Depends(database.get_db)):
    user = services.verify_account(request.username, request.password, database)

    if not user:
        raise HTTPException(
            status_code=400,
            detail='Email or password is incorrect'
        )
    access_token = token.create_access_token(data={"sub": user.email})
    return schema.Token(access_token=access_token, token_type="bearer")



@router.put('/edit/{user_id}', response_class=Response)
async def edit_user(user_id: int, request: schema.User, database: Session = Depends(database.get_db), current_user: User = Depends(get_current_user)):
    return services.edit_user(user_id, request, database)

@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_user_registration(request: schema.User, database: Session = Depends(database.get_db), current_user: User = Depends(get_current_user)):
    user = validator.verify_email_exist(request.email, database)

    if user:
        raise HTTPException(
            status_code=400,
            detail='Email đã được sử dụng.'
        )
    new_user = await services.new_user_register(request, database)
    return new_user

@router.get('/', response_model=List[schema.DisplayUser])
async def get_all_user(database: Session = Depends(database.get_db), current_user: User = Depends(get_current_user)):
    return await services.all_users(database)

@router.get('/{user_id}', response_model=schema.DisplayUser)
async def get_user_by_id(user_id: int, database: Session = Depends(database.get_db), current_user: User = Depends(get_current_user)):
    return await services.get_user_by_id(user_id, database)

@router.delete('/{user_id}', response_class=Response)
async def delete_user(user_id: int, database: Session = Depends(database.get_db), current_user: User = Depends(get_current_user)):
    return services.delete_user(user_id, database)
