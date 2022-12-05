from django.contrib import admin

# Register your models here.
from .models import Contact
# Register your models here.

# register models in our admin panel
# admin.site.register(Blog)
admin.site.register(Contact)