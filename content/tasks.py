from datetime import timedelta
from django.utils import timezone
from celery import shared_task
from content.models import Story


@shared_task
def delete_old_stories():
    # Delete stories older than 24 hours
    threshold_time = timezone.now() - timedelta(hours=24)
    Story.objects.filter(created_at__lt=threshold_time).delete()
