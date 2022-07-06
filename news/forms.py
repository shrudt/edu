from django import forms

from .models import Comments, News


class AddNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'content', 'tag',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Title"}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Content"}),
            'tag': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'})
        }


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Leave a comment'}))

    class Meta:
        model = Comments
        fields = ('content', )



