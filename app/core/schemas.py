from typing import Literal
from uuid import UUID

from pydantic import BaseModel


class BaseModelOut(BaseModel):
    id: UUID

class GeoPoint(BaseModel):
    type: Literal['Point']
    coordinates: tuple[float, float]