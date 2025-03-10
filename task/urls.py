from django.urls import path
from .views import home, addTask, updateTask, deleteTask
urlpatterns = [
    path('',home, name='homepage'),
    path('addTask',addTask, name='addpage'),
    path('updateTask/<int:pk>',updateTask, name='updatepage'),
    path('deleteTask/<int:pk>',deleteTask, name='deletepage'),
]