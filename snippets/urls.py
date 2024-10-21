from django.urls import path
from snippets import views

urlpatterns = [
    path(r"snippets/", views.snippet_list),
    path(r"snippets/<int:pk>/", views.snippet_detail),
]
