from attr import dataclass
from pydantic import BaseModel

class GenerateImageRequest(BaseModel):
    prompt: str