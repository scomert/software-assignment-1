from django.conf.urls import url

from .views import get_entries_of_a_user, get_all_entries_admin, get_all_entries, get_specific_entry, create_new_entry


urlpatterns = [
    url(r'^entries/$', get_all_entries, name="entries"),
    url(r'^entries/(?P<todo_id>[0-9]+)/$', get_specific_entry, name="specific"),
    url(r'^create/$', create_new_entry, name="create"),
    url(r'^entries/all/$', get_all_entries_admin, name="admin-entries"),
    url(r'^entries/all/user/(?P<user_id>[0-9]+)/$', get_entries_of_a_user, name="user-specific-entries"),
]
