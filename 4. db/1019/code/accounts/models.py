from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# 커스텀 User 모델 적용하기
class User(AbstractUser):
    pass