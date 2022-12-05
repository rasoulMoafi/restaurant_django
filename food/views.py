from django.shortcuts import render
from .models import foods

# Create your views here.

def food_list(request):
    food_list = foods.objects.all()
    context ={
        "food" : food_list
    }
    return render(request, "food/list.html",context)


def food_detail(request,id):
    food = foods.objects.get(id=id)
    context = {
        "food" : food
    }
    return render(request,'food/detail.html', context)


# def food_detail(request):     #this funtion is link the headear items
#     food = foods.objects.all()
#     context = {
#         "food" : food
#     }
#     return render(request,'partilas/_header.html', context)