from django.urls import path
from planner import views

urlpatterns = [
    path('', views.tasks_list),
]

