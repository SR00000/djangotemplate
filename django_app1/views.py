from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'insert_me':"Hello I am from django_app1/index.html views.py !"}
    return render(request,'django_app1/index.html',context=my_dict)
