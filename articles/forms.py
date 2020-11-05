from django import forms

from .models import Comment

class AddComment(forms.ModelForm):

    def __init__(self, *a, **kw):
        self.article = kw.pop('article', None)
        return super().__init__(*a, **kw)

    def save(self):
        self.instance.article = self.article
        return super().save()
        
    class Meta:
        model = Comment
        fields = ('author_name', 'author_email', 'comment_text')
        widgets = {
            'author_name': forms.TextInput(attrs={'class': 'full-width'}),
            'author_email': forms.TextInput(attrs={'class': 'full-width'}),
            'comment_text': forms.Textarea(attrs={'class': 'full-width'}),
        }