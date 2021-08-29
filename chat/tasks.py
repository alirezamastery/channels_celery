from __future__ import absolute_import, unicode_literals

from celery.utils.log import get_task_logger
from celery import shared_task
from .models import SomeData


logger = get_task_logger(__name__)


@shared_task
def add(x, y):
    print(f'result of add is {x + y}')
    return x + y


@shared_task
def increment_some_data():
    some_data = SomeData.objects.first()
    some_data.num += 1
    some_data.save()
    logger.info(f'some_data is: {some_data}')
