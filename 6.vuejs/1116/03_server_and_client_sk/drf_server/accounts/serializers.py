from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # password는 조회할 땐 보이지 않도록 (입력은 받되, 출력은 하지 않음)
    ## postman으로 확인 가능
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'password',)