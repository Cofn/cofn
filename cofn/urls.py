"""cofn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views

from cofn.apps.blog.views import home
from cofn.apps.authentication import views as signup_view
from cofn.apps.core import views as core_view


urlpatterns = [
    url(r'^$', core_view.home, name='home'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', signup_view.signup, name='signup'),
    url(r'^admin/', admin.site.urls),
    #url(r'^$', 'cofn.apps.services.views.home_page'),
    #url(r'^services/', include('cofn.apps.services.urls')),
    url(r'^blog/', include('cofn.apps.blog.urls'))
    #url(r'^$', RedirectView.as_view(url='/cofn/apps/services/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
