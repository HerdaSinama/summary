import base64
import logging
from uuid import UUID

from app.core.celery import celery
from app.core.yandex_img import client, model_name
from app.model.enum import ImageGenerationStatus

from .services.db import get_data, update_status
from .services.s3 import upload_to_storage

logger = logging.getLogger(__name__)


@celery.task(
    bind=True,
    acks_late=True,
    max_retries=3,
    rate_limit="10/s",
)
def generate_image_task(self, image_id: str | None = None):
    img_uuid = UUID(str(image_id))
    update_status(img_uuid, status=ImageGenerationStatus.IN_PROGRESS)

    try:
        prompt = get_data(img_uuid)

        api_response = client.images.generate(
            model=model_name,
            prompt=prompt,
            size="1024x1024",
        )

        img_bytes = base64.b64decode(api_response.data[0].b64_json)
        file_key = upload_to_storage(img_bytes, filename=f"{img_uuid}.png")

        update_status(
            img_uuid,
            status=ImageGenerationStatus.COMPLETED,
            img_url=file_key,
        )
        return {"status": ImageGenerationStatus.COMPLETED, "img_url": file_key}

    except Exception:
        logger.exception(f"Error generating image for {img_uuid}")
        update_status(
            img_uuid,
            status=ImageGenerationStatus.FAILED,
        )
        raise
