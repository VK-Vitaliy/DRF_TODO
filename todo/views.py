from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from todo.models import Project
from todo.serializers import ProjectModelSerializer, ToDoModelSerializer


# Create your views here.
class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ToDoModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ToDoModelSerializer
