from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='match_results_index'),
    path("<int:pk>/edit/", views.edit_match, name="match_results_edit"),
    path("<int:pk>/delete/", views.delete_match, name="match_results_delete"),
]
