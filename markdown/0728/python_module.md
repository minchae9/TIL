###### #0728

# 1. 모듈과 패키지

### 모듈

> 특정 기능을 파이썬 파일(.py) 단위로 작성한 것

### 패키지

> - 여러 모듈의 집합
> - 패키지는 다른 패키지를 서브 패키지로 포함할 수 있다.

- PSL(Python Standard Library, 파이썬 표준 라이브러리)

  파이썬에 기본적으로 설치된 모듈과 내장함수

  *라이브러리(library)*: 모듈과 패키지들의 집합

  

  이외에 외부 패키지를 설치하여 third-party 라이브러리를 사용할 수 있다.

## 패키지

#### 패키지 설치

> pip install beautifulsoup4

- 패키지명 뒤에 `==버전넘버`를 적어서 특정 버전을 설치하거나, `>=버전넘버`를 적어서 최소 버전을 명시할 수 있다.
- bash와 cmd 환경에서 실행한다.

#### 패키지 삭제

> pip uninstall beautifulsoup4

#### 패키지 목록 및 특정 패키지 정보

> pip list
>
> pip show beautifulsoup4

#### 패키지freeze

> pip freeze

- 설치된 패키지의 목록을 보여준다.

  > pip freeze > requirements.txt

- 패키지 목록을 텍스트 파일(.txt)로 저장할 수 있다.

  > pip install -r requirements.txt

- 저장된 텍스트 파일 내 패키지대로 자동으로 설치할 수 있다 - 환경 설정

#### 패키지 특징

- 패키지 아래에 `_ _init _ _.py` 파일을 만들어서 패키지로 인식시켜야 한다. Python 3.3부터 요구사항이 아니게 되었지만, 하위 버전과의 호환 및 프레임워크 동작을 고려하여 파일을 생성하기로 한다.

## 모듈

#### 모듈 사용법

```python
import module
from module import var, function, Class
from module import *

from package import module
from package.module import var, function, Class
```

- 모듈 또는 함수의 이름이 길거나 겹치면, `as` 키워드를 통해 해당 환경에서 이름을 바꿔 사용할 수 있다.

# 2. 가상환경

여러 개의 프로젝트를 할 경우, 여러 버전의 라이브러리를 사용할 수 있다.

이때, 프로젝트 별로 별도의 가상환경을 설정하여 패키지와 모듈을 관리할 수 있다.

-> **venv** 를 사용함

- 가상환경은 **독립적인** 공간! global의 영향을 받지 않음.

#### 가상환경 생성

> python -m venv <u>venv</u> 

​		(밑줄은 venv의 이름 설정: 관습적으로 venv라고 씀)

#### 가상환경 활성화/비활성화

* *참고*: Tab키로 자동완성 써서 적기

> (venv 설치경로)/Scripts/Activate

