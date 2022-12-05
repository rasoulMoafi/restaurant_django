from django.db import models
from django.utils.translation import gettext as _


# Create your models hmere.
class Contact(models.Model):
    name = models.CharField(_("نام کاربر"), max_length = 100)
    email = models.EmailField(_("آدرس الکترونیکی"))
    message = models.TextField(_("متن نظر"))

    def __str__ (self):
        return self.email