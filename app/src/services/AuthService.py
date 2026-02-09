from app.src.repositories.AuthRepository import AuthRepository

class AuthService:
    def __init__(self, repo: AuthRepository):
        self.repo = repo

    def store(self, attr: dict):
        return self.repo.create(attr)