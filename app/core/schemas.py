from typing import Literal, Tuple
from uuid import UUID
from pydantic import BaseModel
from shapely.geometry import Point as ShapelyPoint

class BaseModelOut(BaseModel):
    id: UUID

class GeoPoint(BaseModel):
    type: Literal['Point']
    coordinates: Tuple[float, float]