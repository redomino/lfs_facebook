from django.conf.settings import VIEW_WITH_LOGIN_REQUIRED
from django.contrib.auth.decorators import login_required

def permissions_required(perm):
    """
    If you want force user login for a view, 
    you have to set True the corrispondente element 
    in facebook_settings
    """
    def decorator(func):
        if VIEW_WITH_LOGIN_REQUIRED[perm]:
            return login_required(func)
        else:
            return func

    return decorator
