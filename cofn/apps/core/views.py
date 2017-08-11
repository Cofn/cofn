from django.shortcuts import render

from cofn.apps.blog import views as blog_view
import django.contrib.auth.views as login_view
from django.shortcuts import redirect


def home(request):
    if request.user.is_authenticated():
        return blog_view.home(request)
    else:
        return redirect(login_view.login)
