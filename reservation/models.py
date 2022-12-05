from django.db import models
from django.utils.translation import gettext as _  

# Create your models here.
class reservation(models.Model):
    name = models.CharField(_("نام و نام خانوادگی"), max_length = 200)
    email = models.EmailField(_("آدرس الکترونیکی"), max_length = 254)
    phone = models.CharField(_("تلفن"), max_length = 50)
    number = models.IntegerField(_("تعداد"))
    date = models.DateField(_("تاریخ"))
    time = models.TimeField(_("زمان"))

    def __str__(self):
        return self.email