from django.conf.urls import url, include

from .views import signup, login

urlpatterns = [
    url(r'^register/$', signup),
    url(r'^login/$', login),
    url(r'', include("django.contrib.auth.urls")),

]
