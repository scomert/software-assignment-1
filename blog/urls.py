from django.conf.urls import url

from .views import get_all_entries, get_specific_entry, create_new_entry

urlpatterns = [
    url(r'^entries/$', get_all_entries, name="entries"),
    url(r'^entries/(?P<todo_id>[0-9]+)/$', get_specific_entry),
    url(r'^create/$', create_new_entry, name="create"),
]
