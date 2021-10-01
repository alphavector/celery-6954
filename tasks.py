import time

from celery import Celery

app = Celery('tasks', broker='pyamqp://rabbitmq:5672')


@app.task
def add(x, y):
    return f"sum= {x + y}"


@app.task
def sleep(seconds):
    time.sleep(seconds)
    return f"Sleep for {seconds} seconds"


@app.task
def count_of_args(*args, **kwargs):
    return f"args={len(args)}, kwargs={len(kwargs.keys())}"
