from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.subPage, name="entrypage"),
    path("wiki/error", views.subPage, name="errorpage"),
    path("search", views.search, name="search"),
    path("newpage", views.newpage, name="newpage"),
    path("randompage", views.randompage, name="randompage")
]
