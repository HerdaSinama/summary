from app.core.schemas import BaseModelOut, GeoPoint


class SchoolModel(BaseModelOut):
    name: str
    adderss: str
    type: str
    geom: GeoPoint
