
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('typography/', views.typography, name='typography'),
    path('starter/', views.starter, name='starter'),
    path('shop', views.shop, name='shop'),
    path('testimonials', views.testimonials, name='testimonials'),

]
