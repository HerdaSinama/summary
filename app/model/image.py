from sqlalchemy.orm import Mapped, mapped_column

from app.core.model import Base

class Image(Base):
    __tablename__ = 'image'

    status: Mapped[str] = mapped_column()
    prompt: Mapped[str] = mapped_column()
    img_url: Mapped[str | None] = mapped_column(nullable=True)