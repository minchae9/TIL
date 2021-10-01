T = int(input())
for t in range(1, T+1):
    sheet, times = map(int, input().split())
    sheet = list(map(int, str(sheet)))
    # 최고 금액
    new_sheet = sorted(sheet, reverse=True)
    cnt = 0
    flag = False

    # 바꿔야 하는 최소 횟수를 cnt/2
    for i in range(len(sheet)):
        if sheet[i] != new_sheet[i]:
            cnt += 1
    # 최소 횟수보다 더 교환해야 하면
    # 남은 횟수를 leftover에 저장
    if times >= cnt/2:
        if cnt/2 == cnt//2:
            leftover = times - cnt//2
        else:
            leftover = times - (cnt//2+1)
        # 중복 숫자 있으면 그 숫자들끼리 바꾸기 -> 변화 없음.
        for k in range(len(sheet)):
            if new_sheet[k] in new_sheet[k + 1:]:
                flag = True
                break
        # 중복 숫자 없으면, 끝 두 자리수 바꾸기
        if not flag:
            if leftover % 2:
                new_sheet[-1], new_sheet[-2] = new_sheet[-2], new_sheet[-1]
        ans = 0
        for c in range(len(new_sheet) - 1, -1, -1):
            ans += new_sheet[c] * (10 ** (len(new_sheet) - 1 - c))
        print(f'#{t} {ans}')
    # 최대 금액이 되기 위한 최소 횟수보다 적게 교환할 수 있다면
    else:
        # 앞에서부터 뒤의 최대숫자와 교환한다. (이때, 최대 숫자 겹친다면 뒤에 있는 것부터)
        for j in range(len(sheet)):
            if sheet[j] != new_sheet[j]:
                mx = max(sheet[j:])
                mx_idx = len(sheet) - 1 - sheet[::-1].index(mx)
                sheet[j], sheet[mx_idx] = sheet[mx_idx], sheet[j]
                times -= 1
                if times <= 0:
                    ans = 0
                    for d in range(len(sheet) - 1, -1, -1):
                        ans += sheet[d] * (10 ** (len(sheet) - 1 - d))
                    print(f'#{t} {ans}')
                    break
            else:
                continue