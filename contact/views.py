from django.shortcuts import render
from .form import ContactForm
from .models import Contact

# Create your views here.


def contact(request):
    contact = Contact.objects.all()
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['name']
            new_email = form.cleaned_data['email']
            new_message = form.cleaned_data['message']

            new_comment = Contact(name = new_name,email = new_email,message = new_message)
            new_comment.save()
    else:
        new_comment = ContactForm()
    context = {
        "new_comment" : new_comment
    }
    return render(request,'contact/contact.html',context)