from django.http import Http404
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse

from tags.models import Tag
from .models import entries, Entry
from .forms import EntryForm


def get_all_entries(request):
    entry = Entry.objects.all()

    if request.user.is_authenticated:
        user = request.user
        entry = Entry.objects.filter(user=user.id)

        print entry, "Entry", user.id
        return render(request, "my_entries.html", {"entries": entry, "user": user})

    return render(request, "my_entries.html", {"entries": entry, "user": request.user})


def get_specific_entry(request, todo_id):
    entry = Entry.objects.get(pk=todo_id)
    return render(request, "entry.html", {"entry": entry})


def create_new_entry(request):
    if request.user.is_authenticated:
        form = EntryForm()
        tags = Tag.objects.all()
        if request.method == "POST":
            # selected_tag = []
            # new_entry = Entry(user_id=request.user.id, title=request.POST.get("title"), text=request.POST.get("text"))
            # new_entry.save()
            # for i in range(1, len(tags) + 1):
            #     if str(i) in request.POST:
            #         selected_tag.append(int(i))
            # new_entry.tags.add(*selected_tag)
            f = EntryForm(request.POST)
            entry = f.save(commit=False)
            entry.user_id = request.user.id
            entry.save()
            f.save_m2m()
            return redirect(reverse("entries"))
        return render(request, "create_entry.html", {"tags": tags, "form": form})
    else:
        return Http404("You have to be logged in")
