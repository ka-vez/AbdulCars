from django.urls import path
from . import views

# Create your urls here.
urlpatterns = [
    path('', views.home, name='home'),
    path('brand/<str:brand_slug>/', views.car_brands, name ='all-car-brands'),
    path('car/<str:car_slug>/', views.car_info, name='car-info'),
    path('search/', views.search_car, name='search-cars'),
    path('all-brands/', views.all_brands, name='all-brands'),
    path('admin_page/', views.admin_page, name='admin-page'),
    path('update_cars/<int:pk>', views.update_cars, name='update-cars'),
    path('delete-cars/<int:pk>', views.delete_cars, name ='delete-cars'),
    path('add-cars', views.add_car, name = 'add-car'),
    path('update-brand/<int:pk>', views.update_brand, name='update-brand'),
    path('delete-brand/<int:pk>', views.delete_brand, name ='delete-brand'),
    path('add-brand', views.add_brand, name = 'add-brand'),
    path('admin-login', views.admin_login, name = 'admin-login'),
    
]