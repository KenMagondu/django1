from django.urls import path

from teachers import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('about', views.About, name="About"),
    path('contact', views.Contact, name="Contact")

]