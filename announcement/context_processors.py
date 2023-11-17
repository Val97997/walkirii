# announcement/context_processors.py
from .decorators import is_instructor

def custom_context(request):
    return {'is_instructor_user': is_instructor(request.user)}