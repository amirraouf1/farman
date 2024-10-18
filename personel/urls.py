from django.urls import path
from . import views

urlpatterns = [
    path('', views.personnel_list, name='personnel_list'),
    path('add/', views.AddPersonnelView.as_view(), name='add_personnel'),
]
