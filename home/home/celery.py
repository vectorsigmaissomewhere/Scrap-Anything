import os
from celery import Celery
from celery.schedules import crontab 

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'home.settings')

app = Celery('home')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# Namespace 'CELERY_' means all celery-related config keys
# should have a 'CELERY_' prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks() # this wil check if there is any task 

app.conf.beat_schedule = {
    'multiply-task-crontab': {
        "task": "multiply_two_numbers", 
        "schedule": crontab(hour=7, minute=30, day_of_week=1), 
        "args": (16, 16),
    },
    "multiply-every-5-seconds": {
        "task": "multiply_two_numbers",
        "schedule": 5.0,  # Missing comma fixed
        "args": (16, 16),
    },
    "add-every-30-seconds": {
        "task": "movies.tasks.add",
        "schedule": 30.0,
        "args": (16, 16),
    }
}