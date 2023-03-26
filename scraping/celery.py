import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scraping.settings")
app = Celery("scraping", broker=settings.CELERY_BROKER)
app.conf.timezone = "UTC"
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'add-every-monday-morning': {
        'task': 'hackernews_rss',
        'schedule': crontab(minute='*/2'),
    },
}
