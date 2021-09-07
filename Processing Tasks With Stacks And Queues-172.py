## 3. Processing Applications ##

import pandas
applications = pandas.read_csv("applications.csv")
from datetime import datetime

def process_application(application):
    birth_date = datetime.strptime(application["birthdate"], "%Y-%m-%d %H:%M:%S")
    delta = (datetime.now() - birth_date).total_seconds()
    delta /= (3600 * 24 * 365.25)
    if delta < 18:
        return False
    state = application["address"].split(" ")[-2]
    if state != "CA":
        return False
    return True

application_status = list(applications.apply(process_application, axis=1))

## 4. Stacks ##

import threading
import math
import time

def process_application(application):
    time.sleep(.001)
    birth_date = datetime.strptime(application["birthdate"], "%Y-%m-%d %H:%M:%S")
    delta = (birth_date - datetime.now()).total_seconds()
    delta /= (3600 * 24 * 365.25)
    if delta < 18:
        return False
    state = application["address"].split(" ")[-2]
    if state != "CA":
        return False
    return True
wait_times = []
stack = []
task_numbers = []

def add_tasks():
    for index, row in applications.iterrows():
        stack.insert(0,(index + 1, row))
        task_numbers.append(index + 1)
        time.sleep(.001)

def process_tasks():
    tasks_finished = 0
    while tasks_finished < 2400:
        if len(stack) == 0:
            time.sleep(1)
        else:
            task_number, application = stack.pop(0)
            resp = process_application(application)
            tasks_finished += 1
            if task_number == task_numbers[-1]:
                wait_times.append(600)
            else:
                wait_times.append((24 - math.ceil(task_number / 300)) * 3600)
                
t1 = threading.Thread(target=add_tasks)
t2 = threading.Thread(target=process_tasks)

t1.start()
t2.start()
for t in [t1,t2]:
    t.join()

average_wait_time = sum(wait_times) / len(wait_times)
print(average_wait_time)