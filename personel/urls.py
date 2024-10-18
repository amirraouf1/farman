from django.urls import path
from . import views

urlpatterns = [
    path('', views.PersonnelListView.as_view(), name='personnel_list'),
    path('add/', views.PersonnelCreateView.as_view(), name='add_personnel'),
]
