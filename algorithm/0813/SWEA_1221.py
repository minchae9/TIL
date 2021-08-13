T = int(input())
for t in range(T):
    tc, q = input().split()
    number = input().split()
    times = [0]*10
    for num in number:
        if num == 'ZRO':
            times[0] += 1
        elif num == 'ONE':
            times[1] += 1
        elif num == 'TWO':
            times[2] += 1
        elif num == 'THR':
            times[3] += 1
        elif num == 'FOR':
            times[4] += 1
        elif num == 'FIV':
            times[5] += 1
        elif num == 'SIX':
            times[6] += 1
        elif num == 'SVN':
            times[7] += 1
        elif num == 'EGT':
            times[8] += 1
        else:
            times[9] += 1
    answer = 'ZRO '*times[0] + 'ONE '*times[1] + 'TWO '*times[2] + 'THR '*times[3] \
             + 'FOR '*times[4] + 'FIV '*times[5] + 'SIX '*times[6] + 'SVN '*times[7] \
             + 'EGT '*times[8] + 'NIN '*times[9]
    print(tc)
    print(answer)