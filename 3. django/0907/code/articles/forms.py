from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta: # form에 대한 정보
        model = Article
        fields = '__all__'
        # fields = ['title', 'content'] # 전부 다 적어주는 게 권장사항
        # fields = ('title', 'content')
        # exclude = ('title',)  # 제외할 필드
        ## 참고: 튜플에 원소 하나일 땐 , 적어주기 (안 적으면 그냥 문자열과 같음)