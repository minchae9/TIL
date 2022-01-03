T = int(input())
for tc in range(T):
    pars = input()
    cnt = 0
    if len(pars) % 2:
        print('NO')
    else:
        for par in pars:
            if par == '(':
                cnt += 1
            else:
                cnt -= 1
            if cnt < 0:
                print('NO')
                break
        else:
            if cnt == 0:
                print('YES')
            else:
                print('NO')