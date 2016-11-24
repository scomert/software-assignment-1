from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import entries

def get_all_entries(request):
    return render(request, "my_todos.html", {"entries": entries})


def get_specific_entry(request, todo_id):
    try:
        return render(request, "entry.html", {"entry":entries[int(todo_id)]})
    except IndexError:
        raise Http404("We don't have any.")