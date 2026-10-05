from enum import Enum, StrEnum


class ImageGenerationStatus(StrEnum):
    PENDING = "pending"
    QUEUED = "queued"
    IN_PROGRESS = "in_progress"
    FAILED = "failed"
    CANCELLED = "cancelled"
    COMPLETED = "completed"
