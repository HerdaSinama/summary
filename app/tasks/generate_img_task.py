import base64
import logging
from uuid import UUID

from app.core.yandex_img import client, model_name
from app.core.db.sync_db import get_sync_session
from app.model.image import Image
from app.core.celery import celery

logger = logging.getLogger(__name__)


@celery.task(bind=True, acks_late=True, max_retries=3)
def generate_image_task(image_id: str | None = None):
    img_uuid = UUID(str(image_id))
    update_status(img_uuid, status="in_progress")

    try:
        prompt = get_data(img_uuid)

        api_response = client.images.generate(
            model=model_name,
            prompt=prompt,
            size="1024x1024",
        )

        img_bytes = base64.b64decode(
            api_response.data[0].b64_json
        )

        img_url = upload_to_storage(
            img_bytes,
            filename=f"{img_uuid}.png",
        )

        update_status(
            img_uuid,
            status="completed",
            img_url=img_url,
        )
        return {"status": "completed", "img_url": img_url}

    except Exception as exc:
        logger.exception(f"Error generating image for {img_uuid}: {exc}")
        update_status(
            img_uuid,
            status="failed",
        )
        raise exc

def update_status(
        id: UUID,
        status: str,
        img_url: str | None = None,
):
    with get_sync_session() as db:
        image = db.get(Image, id)
        
        if not image:
            raise ValueError(f"Image {id} not found")

        image.status = status

        if img_url is not None:
            image.img_url = img_url

        db.commit()

def get_data(id: UUID):
    with get_sync_session() as db:
        image = db.get(Image, id)

    if not image:
        raise ValueError(f"Image {id} not found")

    prompt = image.prompt

    return prompt

def upload_to_storage(img_bytes: bytes, filename: str) -> str:
    #Заглушка
    return f"https://storage.example.com/{filename}"