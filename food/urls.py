from django.urls import path
from . import views 

app_name = 'food'


urlpatterns = [
    path("", views.food_list, name = "foodlist") ,
    path("<int:id>/", views.food_detail, name = "detail") 
]