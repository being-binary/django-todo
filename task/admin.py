from django.contrib import admin
from .models import Task, List, SubTask, Tag
# Register your models here.

admin.site.register(Task)
admin.site.register(List)
admin.site.register(SubTask)
admin.site.register(Tag)

