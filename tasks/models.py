from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class TUser(models.Model):
    chat_id = models.IntegerField()
    username = models.CharField(max_length=200, blank=True, null=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)


class Project(models.Model):
    name = models.CharField(max_length=50)


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    tuser = models.ForeignKey(TUser, on_delete=models.PROTECT, blank=True, null=True)
    types_choices = [('to-do', 'To-Do'), ('notes', 'Notes'), ('read', 'Read')]
    type = models.CharField(max_length=50, choices=types_choices, default='to-do')
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True, null=True)
    done_status = models.BooleanField(default=False)
    project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.PROTECT)
    date_due = models.DateTimeField()
    today = models.BooleanField(default=False)
    tonight = models.BooleanField(default=False)
    sort = models.FloatField()
    created = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)