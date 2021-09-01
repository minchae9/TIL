from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10) # max_length가 필수 -> 위젯
    content = models.TextField()    # max_length가 옵션
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)