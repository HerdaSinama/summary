from fastapi import APIRouter

router = APIRouter(prefix="/v1")

from app.api.v1.image import router as image_router

router.include_router(image_router)