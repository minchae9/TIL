from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ['title', 'completed'] # author 입력 받지 않고 자동 지정해줄 것임
