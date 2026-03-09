from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='league_table_index'),
]
