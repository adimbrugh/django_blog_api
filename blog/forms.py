

from django import forms
from .models import Comment
from .models import Post
from taggit.forms import TagField



class PostForm(forms.ModelForm):
    tags = TagField(help_text="Comma-separated tags")

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


"""
class PostForm(forms.ModelForm):
    tags = TagField(help_text="Comma-separated tags")

    class Meta:
        model = Post
        fields = ["title", "content", "tags"]
"""