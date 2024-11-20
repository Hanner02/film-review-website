"""
Definition of views.
"""

from django.shortcuts import render, redirect
from urllib import request
from app.forms import LogForm
from datetime import datetime
from app.models import LogMessage
from .models import Film
from .forms import SearchForm
import json
from django.http import HttpResponse



def showMessages(request):
    messages=LogMessage.objects.order_by("-log_date")
    return render(request, "reviewlist.html", {"message_list": messages})

def addMessage(request):
    form = LogForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        message = form.save(commit=False)
        message.log_date = datetime.now()
        message.save()
        return redirect("show")   
    else:
        return render(request, "add.html", {"form": form})


def search_films(request):
    query = request.GET.get('q')
    if query:
        films = Film.objects.filter(title__icontains=query)
    else:
        films = Film.objects.all()[:10]
    return render(request, 'search.html', {'films': films})


def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')


