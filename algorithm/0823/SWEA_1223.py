for t in range(1, 11):
    N = int(input())
    eq = input()
    ans = ''
    stack = []
    # 후위 표기법
    for tk in eq:
        if tk == '+':   # '+'인 경우, stack 끝까지 pop하고, 스택에 넣기
            while len(stack) > 0:
                ans += stack.pop()
            stack.append(tk)
        elif tk == '*': # '*'인 경우, '+'가 나오거나 스택이 빌 때까지 pop하고, 스택에 넣기
            while stack:
                if len(stack) == 0 or stack[-1] == '+':
                    break
                ans += stack.pop()
            stack.append(tk)
        else:   # 숫자
            ans += tk
    while len(stack) > 0:   # 끝에 남은 연산자 pop하기
        ans += stack.pop()
    # 계산
    res = 0
    for k in ans:
        if k == '+':    # 덧셈
            opb = stack.pop()
            opf = stack.pop()
            stack.append(opf+opb)
        elif k =='*':   # 곱셈
            opb = stack.pop()
            opf = stack.pop()
            stack.append(opf * opb)
        else:
            stack.append(int(k))
    print(f'#{t} {stack.pop()}')