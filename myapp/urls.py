
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('typography/', views.typography, name='typography'),
    path('starter/', views.starter, name='starter'),
    path('shop', views.shop, name='shop'),
    path('testimonials', views.testimonials, name='testimonials'),
    path('', views.register, name='register'),
    path('login', views.login, name='login'),
    path('vendorlogin', views.vendorlogin, name='vendorlogin'),
    path('vendorregistration', views.vendorregistration, name='vendorregistration'),
    path('uploadimg', views.uploadimg, name='uploadimg'),
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),

]
