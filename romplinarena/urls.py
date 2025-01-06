"""
URL configuration for romplinarena project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Now this is your root URL
    path('ufc/', views.about, name='ufc'),
    path('sumo/', views.contact, name='sumo'),
    path('boxing/', views.boxing, name='boxing'),
    path('wrestling/', views.wrestling, name='wrestling'),
    path('kickboxing/', views.kickboxing, name='kickboxing'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    # UFC related paths
path('ufc/rankings/', views.ufc_rankings, name='ufc_rankings'),
path('ufc/news/', views.ufc_news, name='ufc_news'),
path('ufc/events/', views.ufc_events, name='ufc_events'),

# Sumo related paths
path('sumo/rankings/', views.sumo_rankings, name='sumo_rankings'),
path('sumo/tournaments/', views.sumo_tournaments, name='sumo_tournaments'),
]
