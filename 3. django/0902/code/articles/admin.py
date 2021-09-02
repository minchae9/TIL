from django.contrib import admin
from .models import Article

# Register your models here.
# 사용자 입력만 보이는데, 생성시간, 수정시간도 보고 싶어
class ArticleAdmin(admin.ModelAdmin):   
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at')
    # Article 모델에서 작성한 거 가져옴

admin.site.register(Article, ArticleAdmin)