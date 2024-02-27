from django.urls import path
from . import views


app_name = "page"

urlpatterns = [
    path("home/", views.index, name = "index")
]