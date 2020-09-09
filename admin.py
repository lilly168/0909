from django.contrib import admin
from .models import Blog, Comment

admin.site.register(Blog)
admin.site.register(Comment)

class CommentForm(forms.ModelsFrom):
    body = forms.CharField(label='댓글', widget=forms.Textarea)

    class Meta:
        model = Comment
        fields = ['body']