from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    # Django가 자동으로
    updated_at = models.DateTimeField(auto_now=True)    # 넣어주는 값 - 입력 받지 않음 (수정도 X)

    def __str__(self):
        return self.title