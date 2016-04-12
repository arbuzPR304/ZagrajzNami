from django import forms

from .models import Comment

class CommentForm(forms.Form):
	tekst = forms.CharField(widget=forms.Textarea)