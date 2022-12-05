from django.urls import path
from . import views

app_name = 'reservation'


urlpatterns = [
    path ("",views.reservation,name ="reserve"),
    path ("gallery/",views.gallery,name ="gallery"),
]