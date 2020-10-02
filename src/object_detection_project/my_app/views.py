from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return render(request,'my_app/login.html')


def home(request):
    return HttpResponse('<h1>Home</h1>')


def register(request):
    return render(request,'my_app/register.html')

