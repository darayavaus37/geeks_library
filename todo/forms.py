from django import forms
from todo.models import TodoModels

class TodoForm (forms.ModelForm):
    class Meta:
        model = TodoModels
        fields = "__all__"

