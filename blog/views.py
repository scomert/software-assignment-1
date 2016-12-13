from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import entries, Entry


def get_all_entries(request):
    entry = Entry.objects.all()

    if request.user.is_authenticated:
        user = request.user
        return render(request, "my_entries.html", {"entries": entry, "user": user})

    return render(request, "my_entries.html", {"entries": entry, "user": request.user})


def get_specific_entry(request, todo_id):
    try:
        return render(request, "entry.html", {"entry": entries[int(todo_id)]})
    except IndexError:
        raise Http404("We don't have any.")
