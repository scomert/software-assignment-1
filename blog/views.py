from django.shortcuts import render, redirect

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .models import entries, Entry
from tags.models import Tag


def get_all_entries(request):
    entry = Entry.objects.all()

    if request.user.is_authenticated:
        user = request.user
        entry = Entry.objects.filter(user=user.id)



        print entry, "Entry", user.id
        return render(request, "my_entries.html", {"entries": entry, "user": user})

    return render(request, "my_entries.html", {"entries": entry, "user": request.user})


def get_specific_entry(request, todo_id):
    try:
        return render(request, "entry.html", {"entry": entries[int(todo_id)]})
    except IndexError:
        raise Http404("We don't have any.")


def create_new_entry(request):
    if request.user.is_authenticated:
        tags = Tag.objects.all()
        if request.method == "POST":
            selected_tag = []
            new_entry = Entry(user_id=request.user.id, title=request.POST.get("title"), text=request.POST.get("text"))
            new_entry.save()
            for i in range(1, len(tags) + 1):
                if str(i) in request.POST:
                    selected_tag.append(int(i))
            new_entry.tags.add(*selected_tag)
            return redirect(reverse("entries"))
        return render(request, "create_entry.html", {"tags": tags})
    else:
        return Http404("You have to be logged in")
