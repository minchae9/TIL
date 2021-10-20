# Model Relationship 01

**1:N 관계에 대해 알아보자!**

## Customizing Authentication in Django

### 1. Substituting a custom User model

Django의 내장 User model 이 제공하는 기능이, 상황에 따라서는 적절하지 않을 수 있다.

예로, 기본 User model은 username을 식별 토큰으로 사용하는데, 이밖에 email 필드 등을 식별 토큰으로 활용하고 싶을 수 있다. 

새 프로젝트를 시작한 이후에 User model에 대해 변경사항을 만들려면 기존의 데이터베이스를 모두 날리는 것을 감수해야 하므로, 이런 위험을 무릅쓰지 않아도 되도록 custome User model을 사용함으로써 추후에도 변경사항을 추가할 수 있게끔 만들 수 있다.

**Django에서는 새 프로젝트를 시작하는 경우 커스텀 유저 모델을 설정하도록 강력하게 권장하고 있다.**

**단, 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업이 이루어져야 한다.**

👉 

```python
# accounts/models.py

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

- 내장 User model을 보면 이또한 AbstractUser을 그대로 상속하고 있다.
- 위의 예시는 커스텀 사항을 추가 또는 변경하지 않고, 기능을 유지하면서 내장 유저 모델을 커스텀 유저 모델로 변경하는 것이다.

<br/>

settings.py에서 `AUTH_USER_MODEL`을 정의하여 커스텀 유저 모델로 기본 User model을 오버라이딩 할 수 있다.

```python
# settings.py

AUTH_USER_MODEL = 'accounts.User'
```

- 기본값: 'auth.User'
- 프로젝트가 진행되는 동안에는 <u>변경할 수 없음!<u>

<br/>

User 모델을 새롭게 정의했으니, 1) admin site와 2) User model을 사용하는 모델폼에도 변경이 이루어져야 한다.

```python
# accounts/admin.py

from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```



### 2. Custom user & Built-in auth forms

유저 모델을 변경했으니, 이를 이용하는 모델 폼도 바뀌어야 한다.

→ UserCreationForm(회원가입), UserChangeForm(회원정보 수정)

#### ※ 주의사항

- User model을 사용할 때는 두 가지 방법으로만 한다: ⭐

  1) models.py에서 사용할 때

     ```python
     from django.conf import settings
     
     settings.AUTH_USER_MODEL
     ```

  2) 그 외의 경우

     ```python
     from django.contrib.auth import get_user_model
     
     get_user_model()
     ```

