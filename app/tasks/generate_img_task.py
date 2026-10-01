import base64
import logging
from uuid import UUID

from app.core.yandex_img import client, model_name
from app.core.celery import celery
from .services.db import update_status, get_data
from .services.s3 import upload_to_storage

logger = logging.getLogger(__name__)


@celery.task(bind=True, acks_late=True, max_retries=3)
def generate_image_task(self, image_id: str | None = None):
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

        file_key = upload_to_storage(
            img_bytes,
            filename=f"{img_uuid}.png",
        )

        update_status(
            img_uuid,
            status="completed",
            img_url=file_key,
        )
        return {"status": "completed", "img_url": file_key}

    except Exception as exc:
        logger.exception(f"Error generating image for {img_uuid}: {exc}")
        update_status(
            img_uuid,
            status="failed",
        )
        raise exc