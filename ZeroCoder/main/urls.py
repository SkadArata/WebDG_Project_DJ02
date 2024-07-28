from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('data', views.data),
    path('test/', views.test, name='test-page'),
    path('new', views.new)
]