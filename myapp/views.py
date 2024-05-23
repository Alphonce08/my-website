from django.shortcuts import render, redirect
from django.conf import settings
import os
# Create your views here.


def index(request):
    return render(request, 'index.html')




