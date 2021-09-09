from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import Thumbnail


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    ## 이미지 필드
    # image = models.ImageField(blank=True)
    ## 원본 저장 X, 썸네일만 저장
    # image_thumb = ProcessedImageField(
    #     blank=True,
    #     processors=[Thumbnail(200, 200)],
    #     format='JPEG',
    #     options={'quality': 90}
    #
    ## 원본과 썸네일 모두 저장
    image = models.ImageField(blank=True, upload_to='images/%Y/%m/%d/')
    image_thumbnail = ImageSpecField(
        source='image',  # 원본 이미지 필드명
        processors=[Thumbnail(200, 200)],
        format='JPEG',
        options={'quality': 90}
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title