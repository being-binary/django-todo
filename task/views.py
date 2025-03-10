from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
# Create your views here.

#serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import taskSerializer
from rest_framework import status

@api_view(['GET'])
def apigetTask(request, *args, **qwargs):
    task = Task.objects.all()
    serializer = taskSerializer(task, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def apiaddTask(request, *args, **qwargs):
    serializer = taskSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def apiupdateTask(request, pk, *args, **qwargs):
    task = Task.objects.get(id = pk)
    serializer = taskSerializer(instance = task, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def apideleteTask(request, pk, *args, **qwargs):
    task = Task.objects.get(id = pk)
    task.delete()
    return Response('item deleted successfully')


#standered

def home(request, *args, **kwargs):
    tasks = Task.objects.all()
    return render(request, 'list.html', context={'tasks':tasks})

def addTask(request, *args, **kwargs):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
        
    return render(request, 'addtask.html', context={'form' : TaskForm()})    

def updateTask(request, pk, *args, **kwargs):
    task =  Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect(home)
    return render(request, 'updatetask.html', context={'form':form})    

def deleteTask(request, pk , *args, **kwargs):
    task = Task.objects.get(id=pk)
    if request.method == "POST":
        task.delete()
        return redirect(home)
    return render(request, 'deletetask.html', context={'task': task})