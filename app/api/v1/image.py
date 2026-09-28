from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db.async_db import get_async_session
from app.schemas.image import GenerateImageRequest
from app.model.image import Image
from app.tasks.generate_img_task import generate_image_task


router = APIRouter(
    prefix='/image',
    tags=['image'],
)

@router.post('/generate')
async def generate_image(
    data: GenerateImageRequest,
    async_session: AsyncSession = Depends(get_async_session)
):
    img = Image(
        prompt=data.prompt,
        status='pending',
    )

    await img.save(async_session)

    result = generate_image_task.delay(image_id=str(img.id))

    return {
        "image_id": img.id,
        "status": "pending",
    }


@router.get('/hello')
async def hello():
    return "hello"


@router.get('/{image_id}')
async def get_image_status(
    image_id: UUID,
    async_session: AsyncSession = Depends(get_async_session)
):
    img = await async_session.get(Image, image_id)
    if not img:
        raise HTTPException(status_code=404, detail="Image not found")
    return {
        "image_id": img.id,
        "status": img.status,
        "prompt": img.prompt,
        "img_url": img.img_url,
    }