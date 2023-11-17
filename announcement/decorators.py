# decorators.py
from django.contrib.auth.decorators import user_passes_test

def is_instructor(user):
    return user.groups.filter(name='Instructors').exists()