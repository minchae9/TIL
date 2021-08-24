for t in range(1, 11):
    N = int(input())
    eq = input()
    nw = ''
    stack = []
    # 후위 표기법
    for c in eq:
        if c == '+':
            while stack and (stack[-1] == '+' or stack[-1] == '*'):
                nw += stack.pop()
            stack.append(c)
        elif c == '*':
            while stack and stack[-1] == '*':
                nw += stack.pop()
            stack.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack[-1] != '(':
                nw += stack.pop()
            stack.pop()
        else:   # 숫자
            nw += c
    # 계산
    for c in nw:
        if c == '*':
            opb = stack.pop()
            opf = stack.pop()
            stack.append(opf * opb)
        elif c == '+':
            opb = stack.pop()
            opf = stack.pop()
            stack.append(opf + opb)
        else:
            stack.append(int(c))
    ans = stack.pop()
    print(f'#{t} {ans}')