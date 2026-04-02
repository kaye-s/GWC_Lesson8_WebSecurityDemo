from django.shortcuts import render, redirect
from .models import Login


def home_view(request):
    return render(request, "index.html")