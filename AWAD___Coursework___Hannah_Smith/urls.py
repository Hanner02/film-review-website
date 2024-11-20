"""
Definition of urls for AWAD___Coursework.
"""

from django.urls import path, include
from django.contrib import admin
from app import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',views.home, name="home"),
    path('home/',views.home, name="home"),
    path('search/',views.search_films, name="search_films"),
    path('add/',views.addMessage, name="add"),
    path('reviewlist/',views.showMessages, name="reviewlist"),
    path('login/',views.login, name="login"),
    path('signup/',views.signup, name="signup"),
    
    path('log/', views.addMessage, name="log"),
    path('show/', views.showMessages, name="show"),
]

urlpatterns += staticfiles_urlpatterns()
