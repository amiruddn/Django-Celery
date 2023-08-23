from tasks import *
from time import sleep
from celery import chain
from datetime import datetime, timedelta

start = 1
progressA = 0
progressB = 0
progressC = 0
progressD = 0
progressE = 0
count = 0
x = 0
# # <===== Running by Queue Without Countdown =====>
# while True:
#     progressA = taskA.apply_async(args=[start], queue='q01', countdown=count)
#     progressE = 0
#     if progressA.get() ==1:
#         progressA = 0
#         progressB = taskB.apply_async(args=[start], queue='q01')
#         progressC = taskC.apply_async(args=[start], queue='q01')
#         if progressB.get() ==1 and progressC.get() ==1:
#             progressD = progressD = taskD.apply_async(args=[start, start], queue='q01')
#             progressB = 0
#             progressC = 0
#             if progressD.get() == 1:
#                 progressE = taskE.apply_async(args=[1], queue='q01').get()
#                 progressD = 0

# # <===== Run Once At Same Time =====>
# progressA = taskA.apply_async(args=[], queue='q01')
# progressB = taskB.apply_async(args=[start], queue='q01')
# progressC = taskC.apply_async(args=[start], queue='q01')
# progressD = taskD.apply_async(args=[start, start], queue='q01')
# progressE = taskE.apply_async(args=[start], queue='q01')

# # <===== Run Once with Countdown =====>
# progressA = taskA.apply_async(args=[], queue='q01', countdown=5)
# progressB = taskB.apply_async(args=[start], queue='q01', countdown=7)
# progressC = taskC.apply_async(args=[start], queue='q01', countdown=7)
# progressD = taskD.apply_async(args=[start, start], queue='q01', countdown=4)
# progressE = taskE.apply_async(args=[start], queue='q01', countdown=3)
