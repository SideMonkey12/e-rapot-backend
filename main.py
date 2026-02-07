from sqlalchemy import text
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from app.core.config import settings
from app.db.db import engine

app = FastAPI(title=settings.APP_NAME)

@app.get('/health')
async def health_check():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1+1")).scalar()
        return JSONResponse(
            content={
                'success': True,
                'message': f'Service is up and running on PORT 8000',
                'database': result
            },

            status_code=status.HTTP_200_OK
        )

