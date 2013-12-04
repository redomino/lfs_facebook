# Create your views here.

from django.template.context import RequestContext
from django.shortcuts import render_to_response

def login(request):
    context = RequestContext(request)

    if request.REQUEST.get('next') != None:
        if request.REQUEST.get('next') == u'/product-form-dispatcher':
            return render_to_response('lfs_facebook/login.html', {"next": u'/cart'}, context)
        else:
            return render_to_response('lfs_facebook/login.html', {"next": request.REQUEST.get('next')}, context)        

    return render_to_response('lfs_facebook/login.html', context)
