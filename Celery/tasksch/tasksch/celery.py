from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tasksch.settings')
# # <===== Using Redis Broker =====>
app = Celery('tasksch', broker = 'redis://localhost:6379', backend='redis://localhost:6379')
# # <===== Using RabbitMQ Broker =====>
# app = Celery('queue', broker='amqp://guest:guest@localhost:5672//', backend='rpc://')

app.config_from_object('django.conf:settings', namespace='CELERY')

# app.conf.update(
#     task_concurrency=3,  # Use 5 threads for concurrency
#     worker_prefetch_multiplier=3  # Prefetch 5 task at a time
# )
app.autodiscover_tasks()

