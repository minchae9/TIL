# 시간초과
N = int(input())
q = []
abs_list = []
for _ in range(N):
    x = int(input())
    if x != 0:
        q.append(x)
        if abs(x) not in abs_list:
            abs_list.append(abs(x))
    else:
        if not q:
            print(0)
        else:
            for i in sorted(abs_list, key=lambda t: abs(t)):
                if -i in q:
                    q.remove(-i)
                    ans = -i
                    break
                elif i in q:
                    q.remove(i)
                    ans = i
                    break
            print(ans)
