from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
path("", views.index, name="index"),
path("home/", views.home, name = "home"),
path("program", views.program, name = "program")
]
urlpatterns += staticfiles_urlpatterns()