from __future__ import absolute_import

from celery.task import task
from .models import Feed, Entry
from django.utils import timezone
import datetime


@task(ignore_results=True)
def update_feed():
   for feed in Feed.objects.all():
       if feed.build_date < timezone.now():
                feed.get_entry_data()



