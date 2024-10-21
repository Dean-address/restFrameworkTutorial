from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path(r"snippets/", views.snippet_list),
    path(r"snippets/<int:pk>/", views.snippet_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)
