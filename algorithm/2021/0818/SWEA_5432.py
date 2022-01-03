T = int(input())
for t in range(1, T+1):
    arr = input()
    o = c = cnt = 0
    for i in range(len(arr)):
        if arr[i] == '(':			 # 열린 괄호 +1
            o += 1
        else:
            if arr[i-1] == '(':		 # 레이저 절단
                o -= 1
                cnt += o
            else:					 # 토막 끝남
                o -= 1
                cnt += 1
    print(f'#{t} {cnt}')