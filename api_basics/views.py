from django.shortcuts import render
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from .models import Tasks
from .serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class TaskApiView(APIView):

    def get(self, request):
        
        tasks = Tasks.objects.filter(owner=request.user)
        serializer = TaskSerializer(tasks, many=True)
        
        return Response(serializer.data)

    def post(self, request):
        
        request.data['owner'] = request.user.id
        print(request.data)
        serializer = TaskSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetails(APIView):

    def get_object(self, id, request):
        try:
            return Tasks.objects.filter(owner=request.user).get(pk=id)
        
        except Tasks.AttributeError:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

        except Tasks.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        
        
    def get(self, request, id):
        task = self.get_object(id, request)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    def put(self, request, id):
        task = self.get_object(id, request)
        serializer = TaskSerializer(task, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        task = self.get_object(id, request)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)