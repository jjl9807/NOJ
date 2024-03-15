from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def ping_view(request):
    now = datetime.now()
    formatted_now = now.strftime('%Y-%m-%d %H:%M:%S')
    return HttpResponse(f"Pong!\n{formatted_now}")