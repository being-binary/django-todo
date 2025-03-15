from django import forms
from django.forms import ModelForm
from .models import Task, List, SubTask, Tag

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'

         
class ListForm(forms.ModelForm):

    class Meta:
        model = List
        fields = '__all__'

         
class SubTaskForm(forms.ModelForm):

    class Meta:
        model = SubTask
        fields = '__all__'

         
class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = '__all__'
