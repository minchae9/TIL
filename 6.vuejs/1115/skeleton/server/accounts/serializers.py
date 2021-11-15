from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'password',)
        # passwordConfirmation은 입력된 password와 일치하는지 확인하기 위해 사용되는 것.
        # password는 출력에 포함되지 않도록. 시리얼라이징에는 사용되지만.
