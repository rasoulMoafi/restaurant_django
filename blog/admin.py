# ***name of class in python is pascalcase

from django.contrib import admin
from .models import Blog,Category,Tag,Comments
# Register your models here.

# register models in our admin panel
# admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comments)

class BlogAdmin(admin.ModelAdmin):    #this class is for cahnge in admin panel details
    list_display = ('title', 'created_at','author')  #display tuple value in admin panel
    list_filter = ('author',) 
    search_fields = ("title",) # specified search in wath field
    ordering = ("title",)  #ordering value in admin panel
    date_hierarchy = "created_at"  #giving admin the ability to see values in categories
    # date_hierarchy = "author__date-joined"  
admin.site.register(Blog,BlogAdmin)