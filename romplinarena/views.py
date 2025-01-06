# romplinarena/views.py
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def ufc(request):
    return render(request, 'ufc/rankings.html')

def sumo(request):
    return render(request, 'sumo/rankings.html')

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

# UFC related views
def ufc_rankings(request):
    return render(request, 'ufc/rankings.html')

def ufc_news(request):
    return render(request, 'ufc/news.html')

def ufc_events(request):
    return render(request, 'ufc/events.html')

# Sumo related views
def sumo_rankings(request):
    return render(request, 'sumo/rankings.html')

def sumo_tournaments(request):
    return render(request, 'sumo/tournaments.html')
