from uuid import UUID

from app.core.db.sync_db import get_sync_session
from app.model.image import Image


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