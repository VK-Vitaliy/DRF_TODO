from rest_framework import serializers

from todo.models import Project, ToDo


class ProjectModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ("name", 'rep_url', "users")


class ToDoModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDo
        fields = ("project", "name", 'text', "user", "is_active")
