from celery import Celery

from app.core.config import config


celery = Celery(
    "summary",
    broker=config.CELERY_BROKER_URL,
    backend=config.CELERY_RESULT_BACKEND,
    include=["app.tasks.generate_img_task"],
)

celery.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
    enable_utc=True,

    worker_prefetch_multiplier=1,

    task_acks_late=True,
    task_reject_on_worker_lost=True,

    task_time_limit=300,
    task_soft_time_limit=240,
)