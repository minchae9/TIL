from rest_framework import serializers
from .models import Article, Comment

# 여러 개는 list로 만듦
class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title',)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',) # 입력 안 받아요 -> 입력값 없어도 validation 체크 통과
        # depth = 1   # nested 방법에서, x단계 더 깊이 있는 데이터까지 보여준다.


class ArticleSerializer(serializers.ModelSerializer):
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True) # nested 방법
    
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)    # 댓글 개수 출력
    
    # comment_first = serializers.CharField(source='comment_set.first', read_only=True) # 모델의 __str__에 설정한 값 나옴
    comment_first = CommentSerializer(source='comment_set.first', read_only=True)   # 전체 정보 나옴

    # 만약 댓글 중 id 값이 15 이하인 댓글을 찾고 싶다면?
    comment_filter = serializers.SerializerMethodField('less_15')   # 함수의 결과값을 내용으로 갖는

    def less_15(self, article):
        qs = Comment.objects.filter(pk__lte=15, article=article)
        serializer = CommentSerializer(instance=qs, many=True)
        return serializer.data

    class Meta:
        model = Article
        fields = '__all__'