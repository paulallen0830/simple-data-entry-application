from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('add/', views.add_task, name='add_task'),
    path('toggle_status/<str:task_id>/', views.toggle_status, name='toggle_status'),
    path('delete_task/<str:task_id>/', views.delete_task, name='delete_task'),
]