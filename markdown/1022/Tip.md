의도하는 프로그램을 생각했다면,

1. ERD(개체-관계 다이어그램)를 먼저 그리고
2. 그에 따라 모델을 정의하고 (+ User 모델 커스텀 하고: settings.py 수정과 함께)
3. 모델 필드를 보고, 그 중 사용자 입력 받는 부분을 정리해서 폼을 정의하고
4. view 함수 작성 시, 사용자 입력을 받지 않는 필드가 있는지 고려해서(`.save(commit=False)`) 작성한다.