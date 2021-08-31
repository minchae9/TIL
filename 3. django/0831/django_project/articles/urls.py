from django.urls import path
from . import views

urlpatterns = [
    path('introduce/', views.introduce, name='introduce'),
    path('index/', views.index, name='index'),
    path('greeting/', views.greeting, name='greeting'),
    path('dinner/', views.dinner, name='dinner'),
    path('image/', views.image),
    path('template_language/', views.template_language),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('hello/<name>/', views.hello),
]
