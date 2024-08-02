from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('new/', views.new, name='page2'),
    path('data/', views.data, name='data'),
    path('data2/', views.data2, name='data2'),
]