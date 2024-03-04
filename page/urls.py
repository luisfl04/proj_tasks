from django.urls import path
from . import views


app_name = "page"

urlpatterns = [
    path("home/", views.home, name = "home"),
    path("done/<int:tarefa_id>/", views.done, name = "done")
]