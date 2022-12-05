from django import forms
from .models import Contact 

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length= 100,required = False)  #requires means user can put empty the field or nor
#     email = forms.EmailField(max_length=100)
#     message = forms.CharField(widget=forms.Textarea)
     
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        # fields = ["name","email","message"]   #optional fields
        fields = "__all__"

