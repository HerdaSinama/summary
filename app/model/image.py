from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column

from app.core.model import Base
from app.model.enum import ImageGenerationStatus


class Image(Base):
    __tablename__ = "image"

    status: Mapped[ImageGenerationStatus] = mapped_column(
        SQLEnum(
            ImageGenerationStatus,
            name="image_generation_status",
            values_callable=lambda obj: [e.value for e in obj],
        ),
        default=ImageGenerationStatus.PENDING,
    )
    prompt: Mapped[str] = mapped_column()
    img_url: Mapped[str | None] = mapped_column(nullable=True)
