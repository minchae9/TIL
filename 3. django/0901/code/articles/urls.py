
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('index/', views.index),
    path('', views.index),  # 빈 문자열 -> 기본주소를 의미: 현재는 http://127.0.0.1:8000/articles/ 주소를 의미
    
]
