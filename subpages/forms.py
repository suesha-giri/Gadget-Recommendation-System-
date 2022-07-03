from django import forms
from django.forms import ModelForm
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['rate','comment']
