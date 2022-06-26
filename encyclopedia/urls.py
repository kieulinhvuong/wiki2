from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.subPage, name="entrypage"),
    path("wiki/error", views.subPage, name="errorpage")
]
