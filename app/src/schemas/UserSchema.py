from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    username: str
    fullname: str
    email: str
    password: str = Field(min_length=8, max_length=72)
    role: str
