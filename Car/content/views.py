from django.shortcuts import render, redirect
from .models import Brand, Car
from .forms import CarForm, BrandForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def all_brands(request):
    brands = Brand.objects.all()
    return render(request, 'content/all_brands.html', {'brands': brands})

def car_brands(request, brand_slug):
    brand = Brand.objects.get(slug = brand_slug)
    cars =  brand.car_set.all()
    return render(request, 'content/car_brands.html', {'cars' : cars})

def home(request):
    posts = Car.objects.all().order_by('-created_at')
    return render(request, 'content/home.html', {'posts' : posts})
    
def car_info(request, car_slug):
    cars = Car.objects.get(slug = car_slug)
    return render(request, 'content/car_info.html', {'cars' : cars} )

def search_car(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        cars = Car.objects.filter(name__contains = searched)
        return render(request, 'content/search_car.html', {'searched' : searched, 'cars' : cars})

    else:
        return render(request, 'content/search_car.html', {})
    
def admin_page(request):
    if request.user.is_superuser:
        cars = Car.objects.all()
        brands = Brand.objects.all()
        return render(request, 'admin/admin_page.html', {'cars' : cars, 'brands' : brands})
    else:
        messages.success(request, 'You are not authorized to access this page')
        return redirect('home')

def update_cars(request, pk):
    if request.user.is_superuser:
        cars = Car.objects.get(id = pk)
        form = CarForm(request.POST or None, request.FILES or None, instance=cars)
        if form.is_valid():
            form.save()
            messages.success(request, 'The Car has been successfully Updated.....')
            return redirect('admin-page')

        return render(request, 'admin/update_cars.html', {'form' : form})
    
    else:
        messages.success(request, 'You are not authorized to access this page')
        return redirect('home')

def delete_cars(request, pk):
    if request.user.is_superuser:
        cars = Car.objects.get(id = pk)
        cars.delete()
        messages.success(request, 'The Car has been successfully deleted.....')
        return redirect('admin-page')
    
    else:
        messages.success(request, 'You are not authorized to delete a car')
        return redirect('home')

def add_car(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CarForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                form.save()
                messages.success(request, 'The new car has been added....')
                return redirect('admin-page')
    
        else:
            form = CarForm()

        return render(request, 'admin/add_car.html', {'form' : form})
    
    else:
        messages.success(request, 'You are not authorized to access this page')
        return redirect('home')


def update_brand(request, pk):
    if request.user.is_superuser:
        brand = Brand.objects.get(id = pk)
        form = BrandForm(request.POST or None, request.FILES or None, instance=brand)
        if form.is_valid():
            form.save()
            messages.success(request, 'The Brand has been successfully Updated.....')
            return redirect('admin-page')

        return render(request, 'admin/update_brand.html', {'form' : form})
    
    else:
        messages.success(request, 'You are not authorized to access this page')
        return redirect('home')

def delete_brand(request, pk):
    if request.user.is_superuser:
        brand = Brand.objects.get(id = pk)
        brand.delete()
        messages.success(request, 'The Brand has been successfully deleted.....')
        return redirect('admin-page')
    else:
        messages.success(request, 'You are not authorized to delete a brand')
        return redirect('home')

def add_brand(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = BrandForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                form.save()
                messages.success(request, 'The new brand has been added....')
                return redirect('admin-page')

        else:
            form = BrandForm()

        return render(request, 'admin/add_brand.html', {'form' : form})
    
    else:
        messages.success(request, 'You are not authorized to access this page')
        return redirect('home')


def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate( username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect('admin-page')
        else:
            messages.success(request, 'There was an error logging in, Try Again!')
            return redirect('admin-login')
    else:
        return render(request, 'admin/admin_login.html', {})


    
