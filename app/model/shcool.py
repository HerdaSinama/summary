from geoalchemy2 import Geometry, WKBElement
from sqlalchemy.orm import Mapped, mapped_column

from app.core.model import Base

class Shcool(Base):
    __tablename__ = "school"

    name: Mapped[str] = mapped_column()
    address: Mapped[str] = mapped_column()
    type: Mapped[str] = mapped_column()
    geom: Mapped[WKBElement] = mapped_column(
        Geometry(geometry_type='POINT', srid='4326', spatial_index=False)
    )