from django.conf import settings
from django.contrib.auth.decorators import login_required

def permissions_required(view_name):
    """
    If you want force user login for a view, 
    you have to set True the corrispondente element 
    in facebook_settings
    """
    def decorator(func):
        if settings.VIEW_WITH_LOGIN_REQUIRED[view_name]:
            return login_required(func)
        else:
            return func

    return decorator
