from django.shortcuts import render
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from todo.filters import TodoFilter
from todo.models import Project, ToDo
from todo.serializers import ProjectModelSerializer, ToDoModelSerializer


class ProjectPagination(PageNumberPagination):
    page_size = 10


class ProjectModelViewSet(ModelViewSet):
    serializer_class = ProjectModelSerializer
    queryset = Project.objects.all()
    pagination_class = ProjectPagination

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        projects = Project.objects.all()
        if name:
            projects = projects.filter(name__contains=name)
        return projects


class ToDoPagination(PageNumberPagination):
    page_size = 20


class ToDoModelViewSet(ModelViewSet):
    serializer_class = ToDoModelSerializer
    queryset = ToDo.objects.all()
    pagination_class = ToDoPagination
    filterset_class = TodoFilter

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.is_active = False
            instance.save()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
