from django.shortcuts import render
from food.models import foods
# Create your views here.


def menu_detail(request):
    menu = foods.objects.all()
    context = {
        'menu' : menu
    }

    return render(request,'menu/menu.html',context)
