from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()    # 현재 Meta 클래스에서 찾는 거고
        fields = UserCreationForm.Meta.fields
        # 나머지는 부모의 UserCreationForm.Meta에서 찾음