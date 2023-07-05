from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.Home, name="Home Page"),
    path('ReadMorePage/<slug>', views.ReadMorePage, name="ReadMore Page"),
    path('DishesPage/', views.DishesPage, name="Dishes Page"),
    path('aboutPage/', views.aboutPage, name="about Page"),
    path('MenuPage/', views.MenuPage, name="Menu Page"),
    path('contactUs/', views.contactUs, name="contactUs Page"),
    path('orderPage/', views.orderPage, name="order Page"),
    path('registerPage/', views.registerPage, name="register Page"),
    path('LoginPage/', views.LoginPage, name="Login Page"),
    path('LogoutPage/', views.LogoutPage, name="LogoutPage Page"),
]