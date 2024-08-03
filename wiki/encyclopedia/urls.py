from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>",views.entry,name="entry"),
    path("create",views.create,name="create"),
    path("edit/<str:title>",views.edit_page,name="edit"),
    path("search",views.search,name="search"),
    path("random",views.random_page,name="random"),
]
