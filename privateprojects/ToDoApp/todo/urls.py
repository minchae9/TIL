from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.create, name='create'),
    path('<int:item_pk>/edit/', views.edit, name='edit'),
    path('<int:item_pk>/delete/', views.delete, name='delete'),
    path('<int:item_pk>/', views.check, name='check'),
]