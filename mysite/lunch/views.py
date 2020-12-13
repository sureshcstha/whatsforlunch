from django.shortcuts import render, redirect
from .models import Restaurant
from django.core.paginator import Paginator
import random


# Create your views here.
def index(request):
    restaurant = Restaurant.objects.all()
    random_item = random.choice(restaurant)
    context = {
        'restaurant': random_item
    }
    return render(request, 'lunch/index.html', context)


def about(request):
    context = {}
    return render(request, 'lunch/about.html', context)


def restaurant_list(request):
    restaurant_object = Restaurant.objects.all()
    restaurant_name = request.GET.get('restaurant_name')

    if restaurant_name != '' and restaurant_name is not None:
        restaurant_object = restaurant_object.filter(name__icontains=restaurant_name)

    paginator = Paginator(restaurant_object, 9)
    page = request.GET.get('page')
    restaurant_object = paginator.get_page(page)
    return render(request, 'lunch/restaurant_list.html', {'restaurant_object': restaurant_object})


def add_restaurant(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')
        address = request.POST.get('address', '')
        type_of_food = request.POST.get('type_of_food', '')
        affordability = request.POST.get('affordability', '')
        phone = request.POST.get('phone', '')
        website = request.POST.get('website', '')
        dine_in = request.POST.get('dine_in', '')
        take_out = request.POST.get('take_out', '')
        google_maps_code = request.POST.get('google_maps_code', '')
        image = request.FILES.get('image', '')
        restaurant = Restaurant(name=name, description=description, address=address, type_of_food=type_of_food,
                                affordability=affordability, phone=phone, website=website, dine_in=dine_in,
                                take_out=take_out, google_maps_code=google_maps_code, image=image)
        restaurant.save()

    return render(request, 'lunch/form.html')


def detail(request, restaurant_id):
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    context = {
        'restaurant': restaurant,
    }
    return render(request, 'lunch/detail.html', context)


def update_restaurant(request, id):
    restaurant = Restaurant.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')
        address = request.POST.get('address', '')
        type_of_food = request.POST.get('type_of_food', '')
        affordability = request.POST.get('affordability', '')
        phone = request.POST.get('phone', '')
        website = request.POST.get('website', '')
        dine_in = request.POST.get('dine_in', '')
        take_out = request.POST.get('take_out', '')
        google_maps_code = request.POST.get('google_maps_code', '')
        image = request.FILES.get('image', '')
        restaurant = Restaurant(name=name, description=description, address=address, type_of_food=type_of_food,
                                affordability=affordability, phone=phone, website=website, dine_in=dine_in,
                                take_out=take_out, google_maps_code=google_maps_code, image=image)
        restaurant.save()

    return render(request, 'lunch/form.html')


def delete_restaurant(request, id):
    restaurant = Restaurant.objects.get(id=id)

    if request.method == 'POST':
        restaurant.delete()
        return redirect('index')

    return render(request, 'lunch/delete.html', {'restaurant': restaurant})

