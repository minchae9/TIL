import sys
while True:
    res = sys.stdin.readline().strip('\n')  # sys.stdin.readline()은 개행문자까지 달고 나옴
    if res == '':
        break
    print(res)