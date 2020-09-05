from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=140)
    date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

class Meta:
    ordering = ['completed', 'date']