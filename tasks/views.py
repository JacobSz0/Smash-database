from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tasks.models import Task

@login_required()
def create_recipe(request):
    if request.method == "POST":
        form = Task(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Main")
    else:
        form = Task()
    context = {
        "form": form
    }
    return render(request, "recipes/create.html", context)
