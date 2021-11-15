from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from . import views


urlpatterns = [
    path('signup/', views.signup),
    # JWT 발급 url
    path('api-token-auth/', obtain_jwt_token),  # 형식 맞춰줌

]
