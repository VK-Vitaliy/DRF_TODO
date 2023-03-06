from django.db import models

from usersapp.models import User


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=356)
    rep_url = models.URLField(max_length=200, blank=True)
    users = models.ManyToManyField(User)


class ToDo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=356)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
