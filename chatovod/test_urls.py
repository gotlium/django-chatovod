try:
    from django.conf.urls.defaults import patterns, url
except ImportError:
    from django.conf.urls import patterns, url

from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


urlpatterns = patterns(
    '',
    url(r'^$', home, name='home'),
)
