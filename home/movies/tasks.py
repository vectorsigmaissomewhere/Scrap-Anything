from celery import shared_task 

@shared_task 
def add(x, y): # do not use Django models instances as args , just json data 
    # if I am using models 
    """
    from django.apps import apps 
    MyModel = apps.get_model('app', "model")
    """
    return x + y 

@shared_task(name="multiply_two_numbers")
def mul(x, y):
    # Celery recognizes this as the 'multiple_two_numbers' task 
    total = x * (y * random.randint(3, 100))
    return total 

@shared_task(name="sum_list_numbers")
def xsum(numbers):
    # Celery recognizes this as the 'sum_list_numbers' task 
    return sum(numbers)