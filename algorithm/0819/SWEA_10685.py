T = int(input())
for t in range(1, T + 1):
    s = input()
    stack = [0] * 1000
    top = -1
    for c in s:
        if top < 0 or stack[top] != c:  # i) 스택이 비어있거나, ii) 마지막으로 넣은 요소와 다를 경우
            top += 1
            stack[top] = c
        else:  # 스택에 문자 요소가 있고, 마지막 넣은 요소와 같을 경우
            top -= 1

    print(f'#{t} {top+1}')