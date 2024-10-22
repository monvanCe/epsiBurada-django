import requests
from celery import shared_task

@shared_task
def call_endpoint():
    print('Calling endpoint')