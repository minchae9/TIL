T = int(input())
for t in range(1, T+1):
    s = input()
    stack = []
    ans = 1
    for c in s:
        if c in ['(', '{']:					# 여는 괄호
            stack.append(c)
        elif c in [')', '}']:				# 닫는 괄호
            if not stack:					 # 스택이 비어있으면, ans = 0
                ans = 0
                break
            if c == ')':					 # ')' 인 경우 - 짝이 안 맞으면 ans = 0
                rec = stack.pop()
                if rec != '(':
                    ans = 0
                    break
            else:							 # '}' 인 경우 - 짝이 안 맞으면 ans = 0
                rec = stack.pop()
                if rec != '{':
                    ans = 0
                    break
    if stack:								# 루프가 끝난 stack이 비어있지 않으면 ans = 0
        ans = 0

    print(f'#{t} {ans}')