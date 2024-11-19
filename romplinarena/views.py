# romplinarena/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'ufc.html')

def contact(request):
    return render(request, 'sumo.html')

def boxing(request):
    return render(request, 'boxing.html')

def wrestling(request):
    return render(request, 'wrestling.html')

def kickboxing(request):
    return render(request, 'kickboxing.html')

def profile(request):
    return render(request, 'profile.html')

def register(request):
    return render(request, 'register.html')
