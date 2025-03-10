from django.urls import path
from .views import apigetTask, apiaddTask, apiupdateTask, apideleteTask
urlpatterns = [
    path('alltask/',apigetTask, name='apigetpage'),
    path('createtask/',apiaddTask, name='apiaddpage'),
    path('updatetask/<int:pk>',apiupdateTask, name='apiupdatepage'),
    path('deletetask/<int:pk>',apideleteTask, name='apideletepage'),
]