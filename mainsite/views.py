from django.shortcuts import render
from datetime import datetime


def index(request):
    now = datetime.now()
    return render(request, 'index.html', {'msg': 'Hello'})