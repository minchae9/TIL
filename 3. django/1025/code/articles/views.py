from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404, get_object_or_404, render

from articles.serializers import ArticleListSerializer, ArticleSerializer
from .models import Article

# Create your views here.
@api_view(['GET'])  # 404 에러를 json으로 보내줌 (없으면, HTML로 보여짐)
def article_list(request):
    articles = get_list_or_404(Article) # QuerySet
    serializers = ArticleListSerializer(articles, many=True)   # Serialization
    return Response(serializers.data)

@api_view(['GET'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)
