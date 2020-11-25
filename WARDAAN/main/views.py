from django.shortcuts import render
from django.conf import settings
from django.http import HttpRequest,HttpResponse

def index(request):
    d={}
    response=render(request,'index.html',d)
    return response