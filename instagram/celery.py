import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'instagram.settings')
app = Celery('instagram')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'delete_old_stories': {
        'task': 'content.tasks.delete_old_stories',
        'schedule': crontab(minute='*/1'),  # Run every minute
    },
}
