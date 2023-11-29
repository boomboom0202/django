from django import forms
from .models import *

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text']
        labels = {
            'title': 'Заголовок',
            'text': 'Описание',
        }