# Create your views here.

from django.template.context import RequestContext
from django.shortcuts import render_to_response

def login(request):
    context = RequestContext(request)
#    import pdb; pdb.set_trace();
    if request.REQUEST.get('next') != None:
	    return render_to_response('lfs_facebook/login.html', {"my_next": request.REQUEST.get('next')}, context)
    
    return render_to_response('lfs_facebook/login.html', context)
