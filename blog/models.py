from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

from ckeditor.fields import RichTextField   #this library giving texteditor tools


# Create your models here.
class Blog(models.Model):
    title = models.CharField(_("عنوان"), max_length= 50)
    description = models.CharField(_("توضیحات"), max_length= 100)
    # content = models.TextField(_("متن"))
    content = RichTextField(config_name = "myConfig")
    created_at = models.DateTimeField(_("زمان انتشار"), default = timezone.now)
    author = models.ForeignKey(User, verbose_name=_("نویسنده"), on_delete=models.CASCADE)
    image = models.ImageField(_("تصویر"), upload_to="blogs/", blank = True, null = True)
    category = models.ForeignKey("Category", related_name="blog", verbose_name =_("دسته بندی"), on_delete=models.CASCADE, blank = True, null = True)
    tags = models.ManyToManyField("Tag",verbose_name =_("تگ  ها"),related_name="blogs", blank = True, null = True)
    def __str__ (self):
        return self.title

    #related_name baraye search estefade mishe(bbinim kudum blog ha tu category hastn)

class Category(models.Model):
    title = models.CharField(_("عنوان"), max_length = 50)
    slug = models.SlugField(_("عنوان لاتین"))   #baraye adress dehi(baraye seo khube)
    published_at = models.DateTimeField(_("تاریخ انتشار"), auto_now = False, auto_now_add = True) 
    def __str__ (self):
        return self.title

class Tag (models.Model):
     title = models.CharField(_("عنوان"), max_length = 50)
     slug = models.SlugField(_("عنوان لاتین")) 
     published_at = models.DateTimeField(_("تاریخ انتشار"), auto_now = False, auto_now_add = True) 
     update_at = models.DateTimeField(_("تاریخ انتشار"), auto_now =True , auto_now_add = False) 
     def __str__ (self):
        return self.title
        
class Comments (models.Model):
    blog = models.ForeignKey("Blog",verbose_name=_("مقاله"), related_name ="comments" ,on_delete=models.CASCADE)
    name = models.CharField(_("نام کاربر"), max_length = 100)
    email = models.EmailField(_("آدرس الکترونیکی"))
    message = models.TextField(_("متن نظر"))
    date = models.DateTimeField(_("تاریخ انتشار"), auto_now =False , auto_now_add = True) 

    class Meta:
        verbose_name = 'نظرات'   #change name in admin panel
        verbose_name_plural = "نظرات"      #plural form (for decrease "s" in the admin panel)
    
    def __str__ (self):
        return self.name