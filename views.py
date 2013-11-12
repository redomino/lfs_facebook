# Create your views here.

from django.template.context import RequestContext
from django.shortcuts import render

from django.http import HttpResponse

def login(request):
    context = RequestContext(request)
    return render(request, 'lfs_facebook/login.html', context)

def text_try(request):
    return HttpResponse("Hello, world. You're at the poll index.")
