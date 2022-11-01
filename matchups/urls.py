from django.urls import path
from matchups.views import char_list

urlpatterns = [
    path("", char_list, name="char_list"),
]