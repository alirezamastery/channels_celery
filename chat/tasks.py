from __future__ import absolute_import, unicode_literals

from celery import shared_task
from .models import SomeData


@shared_task
def add(x, y):
    return x + y


@shared_task
def increment_some_data(data):
    some_data = SomeData.objects.first()
    some_data.num += 1
    some_data.save()
    print(f'some_data is: {some_data}')
