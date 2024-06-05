from pydantic import BaseModel, constr, EmailStr



class User(BaseModel):
    first_name: constr(min_length=1)
    last_name: constr(min_length=1)
    phone_number: constr(min_length=10, max_length=10)
    email: EmailStr
    password: str
    def __str__(self):
        return f'{self.email} {self.password}'

class DisplayUser(BaseModel):
    id : int
    first_name : str
    last_name : str
    phone_number : str
    email : EmailStr
    password : str

    class Config:
        from_attributes = True

class LoginUser(BaseModel):
    email : EmailStr
    password : str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: EmailStr | None = None

