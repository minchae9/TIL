T = int(input())

for i in range(T):
    lst = list(input().split(' '))
    times = int(lst[0])
    word = lst[1]
    answer = ''
    for w in word:
        answer += w*times
    print(answer)
    answer = ''