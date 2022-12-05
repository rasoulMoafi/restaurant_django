from django import forms
from .models import reservation

# class ReservationForm(forms.Forms):
#     name = forms.CharField(max_length=200)
#     email = forms.EmailField(max_length=200)
#     phone = forms.IntegerField()
#     ...

class ReservationForm(forms.ModelForm):
    class Meta:
        model = reservation
        # fields = ["name", "email","phone",..]
        fields = "__all__"