T = int(input())
for t in range(1, T+1):
    str1 = set(input())
    str2 = input()
    lett = {}
    mx = 0
    for c in str1:
        lett[c] = 0
        for m in str2:
            if c == m:
                lett[c] += 1
        if lett[c] > mx:
            mx = lett[c]
    print(f'#{t} {mx}')