from celery import Celery,shared_task
from time import sleep

celery_app = Celery('tasksch',
     broker = 'amqp://guest:guest@localhost:5672//',
     backend='rpc://',)
celery_app.conf.update(
    task_concurrency=5,  # Use 5 threads for concurrency
    worker_prefetch_multiplier=5  # Prefetch 5 task at a time
)
progressA = 0
progressB = 0
progressC = 0
progressD = 0
progressE = 0

@celery_app.task
def taskA():
    # if trigger == 1:
    print("starting Task-A")
    sleep(1)
    print("progress...")
    sleep(2)
    print("Task-A completed \n")
    return 1
    # else:
    #     print("parameter A waiting to start...")
    #     sleep(2)

@celery_app.task
def taskB(trigger):
    if trigger == 1:
        print("starting Task-B")
        sleep(1)
        print("progress...")
        sleep(5)
        print("Task-B completed \n")
        return 1
    else:
        print("parameter B waiting to start...")
        sleep(2)

@celery_app.task
def taskC(trigger):
    if trigger == 1:
        print("starting Task-C")
        sleep(1)
        print("progress...")
        sleep(3)
        print("Task-C completed \n")
        return 1
    else:
        print("parameter C waiting to start...")
        sleep(2)

@celery_app.task
def taskD(trigger1, trigger2):
    if trigger1 == 1 and trigger2 == 1:
        print("starting Task-D")
        sleep(1)
        print("progress...")
        sleep(5)
        print("Task-D completed \n")
        return 1
    else:
        print("parameter D waiting to start...")
        sleep(2)

@celery_app.task
def taskE(trigger):
    if trigger == 1:
        print("starting Task-E")
        sleep(1)
        print("progress...")
        sleep(7)
        print("Task-E completed \n")
        return 1
    else:
        print("parameter E waiting to start...")
        sleep(2)

# Other Celery settings
celery_app.conf.beat_schedule = {
    'task-number-one': {
        'task': 'taskA',
        'schedule': 10.0,
    }
}