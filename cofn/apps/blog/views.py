from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PostForm

from .models import Post


#def home(request):
 #   entries = Post.objects.all()[:10]
  #  return render(request, 'index.html', {'posts': entries})


@login_required
def home(request):
    entries = reversed(Post.objects.all()[:10])
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = Post()
            new_post.author = request.user
            new_post.title = form.cleaned_data.get('title')
            new_post.body_text = form.cleaned_data.get('body_text')
            if len(new_post.body_text) > 0:
                new_post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'index.html', {'form': form, 'posts': entries})
