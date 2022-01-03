N = int(input())
words = [0] * N
length = [0] * N
ans = []
for n in range(N):
    words[n] = input()
    length[n] = len(words[n])
# min으로 길이 탐색하여
while True:
    found = set()
    small = min(length)
    if small > 50:
        break
    for l in range(N):
        if length[l] == small:
            found.add(words[l])
            words[l] = 'f'*51
            length[l] = 51
    # 사전순으로 정렬하여 배치
    found = list(found)
    found.sort()    # sort 메서드 만으로 단어를 사전 순으로 정렬할 수 있다.
    ans.extend(found)
# 출력
for item in ans:
    print(item)