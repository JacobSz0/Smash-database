from django.shortcuts import render
from matchups.models import Character


def char_list(request):
    characters = Character.objects.all()
    context = {
        "char_list": characters,
    }
    return render(request, "matchups/list.html", context)
