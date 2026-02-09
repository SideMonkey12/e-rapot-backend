from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.src.services.AuthService import AuthService
from app.src.schemas.UserSchema import UserCreate
from app.db.db import SessionLocal
from app.src.repositories.AuthRepository import AuthRepository

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/register')
async def register(attr: UserCreate, db: Session = Depends(get_db)):
    try:
        repository = AuthRepository(db)
        service = AuthService(repository)
        service.store(attr.model_dump())

        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                'success': True,
                'message': 'User created successfully'
            }
        )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                'success': False,
                'message': str(e)
            }
        )


