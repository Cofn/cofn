from django.shortcuts import render_to_response

from .models import Post


def home(request):
    entries = Post.objects.all()[:10]
    return render_to_response('index.html', {'posts': entries})
