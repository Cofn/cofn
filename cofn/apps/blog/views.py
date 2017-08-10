from django.shortcuts import render_to_response

from .models import Posts


def home(request):
    entries = Posts.objects.all()[:10]
    return render_to_response('index.html', {'posts': entries})
