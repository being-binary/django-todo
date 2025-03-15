from django.db import models
from django.utils.timezone import now

class List(models.Model):
    title = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    completed = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    duedate = models.DateField(null=True, blank=True)
    listtype = models.ForeignKey(List, related_name='tasks', on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        # Ensure a default list is set if no listtype is provided
        if not self.listtype:
            default_list, created = List.objects.get_or_create(title="Default List")
            self.listtype = default_list
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class SubTask(models.Model):
    title = models.CharField(max_length=100)
    task = models.ForeignKey(Task, related_name='subtasks', on_delete=models.CASCADE)  # Allow multiple subtasks per task

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50)  # Renamed field for clarity
    tasks = models.ManyToManyField(Task, related_name='tag')

    def __str__(self):
        return self.name
