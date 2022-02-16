from asyncio import tasks
from urllib import request, response
from django.shortcuts import render
from django . http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Task
from .serializers import TaskSerializer
from api import serializers

# Create your views here.
@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'List':'/task-list', 
        'Detail-View ': '/task-details/<str:pk>/', 
    }
    return Response(api_urls)
@api_view(['GET'])
def Tasklist(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data )

@api_view(['GET'])
def TaskView(request,pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def TaskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Created succesfully!"})
    return Response(serializer.data)

@api_view(['GET','POST'])
def TaskUpdate(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task ,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def TaskDelete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("item delete successfully")

