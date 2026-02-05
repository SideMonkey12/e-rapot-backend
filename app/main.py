from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get('/health')
async def health_check():
    return JSONResponse(
        content={
            'success': True,
            'message': 'Service is up and running on PORT 8000'
        },

        status_code=status.HTTP_200_OK
    )