from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        exclude = ('done',)
        widgets = {
            'task': forms.TextInput(attrs={
                'placeholder': 'Your mission today!',
            	}
            ),
            'time': forms.DateTimeInput(attrs={
                'placeholder': '0000-00-00 24:00',
            	}
            ),
        }

        