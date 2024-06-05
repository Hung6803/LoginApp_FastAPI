from typing import List, Optional, Annotated

from . import models, schema, hashing, validator
from fastapi import HTTPException, status, Depends




async def new_user_register(request: schema.User, database) -> models.User:
    new_user = models.User(first_name=request.first_name, last_name=request.last_name,
                           phone_number=request.phone_number, email=request.email, password=request.password)
    database.add(new_user)
    database.commit()
    database.refresh(new_user)
    return new_user


async def all_users(database) -> List[models.User]:
    users = database.query(models.User).all()
    return users


async def get_user_by_id(user_id, database) -> Optional[models.User]:
    user_info = database.query(models.User).get(int(user_id))
    if not user_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user_info


def delete_user(user_id, database):
    database.query(models.User).filter(models.User.id == user_id).delete()
    database.commit()


def edit_user(user_id, request, database):
    request.password = hashing.get_password_hash(request.password)
    database.query(models.User).filter(models.User.id == user_id).update(request)
    database.commit()


def get_user_by_email(email, database) -> Optional[models.User]:
    user_info = database.query(models.User).filter(models.User.email == email).first()

    return user_info

def verify_account(email, password, database) -> Optional[models.User]:
    user_info = validator.verify_email_exist(email, database)
    if not user_info or not hashing.verify_password(password, user_info.password):
        return None
    else:
        return user_info


