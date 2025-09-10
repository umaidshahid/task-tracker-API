from celery import Celery
from app.core.config import settings

celery = Celery(__name__, broker=settings.REDIS_URL)

@celery.task
def notify_assignment(task_id: int, assignee_id: int):
    # placeholder for sending email/notification
    print(f"Notify assignee {assignee_id} that task {task_id} was assigned")
