from fastapi import FastAPI
from app.api.router import router as api_router

def get_application() -> FastAPI:
    app = FastAPI()

    app.include_router(api_router)

    return app
    
app = get_application()