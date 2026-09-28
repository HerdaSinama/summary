

class ImageGenerationStatus(str, Enum):
    QUEUED = "queued"
    IN_PROGRESS = "in_progress"
    FAILED = "failed"
    CANCELLED = "cancelled"
    COMPLETED = "completed"