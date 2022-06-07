from django.shortcuts import render

# Create your views here.

from .models import meals

def meal_list(request):
    meal_list = meals.objects.all()
    context = {'meal_list' : meal_list,}
    return render(request, 'meals/list.html', context)

def meal_detail(request, slug):
    meal_detail = meals.object.get(slug=slug)
    context = {'meal_detail' : meal_detail}
    return render(request, 'meals/detail.html')