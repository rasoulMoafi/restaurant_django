from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=25)
    message = forms.CharField(widget=forms.Textarea)
