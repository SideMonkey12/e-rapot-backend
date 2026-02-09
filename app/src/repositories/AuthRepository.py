from sqlalchemy.orm import Session
from app.src.models.User import User
from app.core.security import hash_password

class AuthRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, attr: dict):
        user = User(
            username = attr['username'],
            fullname = attr['fullname'],
            email = attr['email'],
            password = hash_password(attr['password']),
            role = attr['role'],
        )

        self.session.add(user)
        self.session.commit()

        return user