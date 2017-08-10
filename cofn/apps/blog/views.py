from django.shortcuts import render_to_response
from .models import Posts

def home(request):
    return render_to_response('index.html')