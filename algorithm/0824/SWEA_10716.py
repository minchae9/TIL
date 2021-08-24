T = int(input())
for t in range(1, T+1):
    eq = input().split()
    stack = []
    for c in eq:
        try:
            if c == '.':  # . 출력
                ans = stack.pop()
            elif c in ['+', '*', '-', '/']:   # 연산자
                opb = stack.pop()
                opf = stack.pop()

                if c == '+':
                    stack.append(opf+opb)
                elif c == '-':
                    stack.append(opf-opb)
                elif c == '*':
                    stack.append(opf*opb)
                else:   # c == '/'
                    stack.append(opf//opb)

            else:   # 숫자
                stack.append(int(c))
        except:
            ans = 'error'
            break
        else:
            if stack:           # 연산 후에도 stack이 비어있지 않으면 (!!주의)
                ans = 'error'

    print(f'#{t} {ans}')