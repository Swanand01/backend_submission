from celery import shared_task


@shared_task
def yolo():
    print("YOLO")
