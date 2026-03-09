from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='match_results_index'),
]
