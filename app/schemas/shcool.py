from pydantic import BaseModel, dataclasses

from app.core.schemas import GeoPoint


@dataclasses
class SchoolModel(BaseModel):
    name: str
    adderss: str
    type: str
    geom: GeoPoint
