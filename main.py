from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from app.src.core.config import settings

app = FastAPI(title=settings.APP_NAME)

@app.get('/')
async def root():
    return {
        'ok': True,
        'env': settings.APP_NAME
    }

@app.get('/health')
async def health_check():
    return JSONResponse(
        content={
            'success': True,
            'message': f'Service is up and running on PORT {settings.APP_PORT}'
        },

        status_code=status.HTTP_200_OK
    )

