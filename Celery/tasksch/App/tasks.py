from celery import Celery,shared_task
from time import sleep
from datetime import datetime, timedelta

celery_app = Celery('tasksch',
     # # <===== Using Redis Broker =====>
     broker = 'redis://localhost:6379',
     backend='redis://localhost:6379')
     # # <===== Using RabbitMQ Broker =====>
     # broker = 'amqp://guest:guest@localhost:5672//',
     # backend='rpc://',)

# celery_app.conf.update(
#     task_concurrency=5,  # Use 5 threads for concurrency
#     worker_prefetch_multiplier=5  # Prefetch 5 task at a time
# )

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
    sleep(5)
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
        sleep(5)
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

# # <===== Task Schedling With Delay After Task Finished =====>
# # input_time[1,2,3,4,5,6,7,8,9,10] <==> output_time[1,4,8,12,16,20,24,28,32,36]
# # output time in seconds = (input_time - 1) * 4 seconds (using RabbitMQ)
# # so to get desired time, input time shoud be (input_time / 4) +1
# desired_time = 5
# fixed_time = (desired_time / 4) +1
# celery_app.conf.beat_schedule = {
#     'task-number-one': {
#         'task': 'App.tasks.taskA',
#         'schedule': timedelta(seconds=fixed_time),
#     }
# }

# # <===== Task Schedling With Delay After Task Started =====>
# # input_time[1,2,3,4,5,6,7,8,9,10] <==> output_time[4,8,12,16,20,24,28,32,36,40]
# # output time in seconds = (input_time * 4 seconds) (using RabbitMQ)
# # so to get desired time, input time shoud be (input_time / 4)
# desired_time = 10
# fixed_time = (desired_time / 4)
# celery_app.conf.beat_schedule = {
#     'task-number-one': {
#         'task': 'App.tasks.taskA',
#         'schedule': fixed_time,
#     }
# }

# # <===== Task Schedling With Delay After Task Started =====>
# celery_app.conf.beat_schedule = {
#     'toggle-tasksA': {
#         'task': 'App.tasks.TaskA',
#         'schedule': 6,
#     },
#     'toggle-tasksB': {
#         'task': 'App.tasks.TaskB',
#         'schedule': 6,
#     },
#     'toggle-tasksC': {
#         'task': 'App.tasks.TaskC',
#         'schedule': 6,
#     },
# }