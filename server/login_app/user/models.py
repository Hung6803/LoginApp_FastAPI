from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from login_app.database import Base
from login_app.user import hashing

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    phone_number = Column(String(10), unique=True)
    email = Column(String(50), unique=True)
    password = Column(String(255))

    def __init__(self, first_name, last_name, phone_number, email, password, *args, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.password = hashing.get_password_hash(password)

    def check_password(self, password):
        return hashing.verify_password(self.password, password)

    def __str__(self):
        return f'{self.email} {self.password}'