# https://swexpertacademy.com/main/learn/course/lectureHtmlViewer.do
# SWEA_SW문제해결 Self Study Book I > Baby Gin Game
T = int(input())
for _ in range(T):
    tc = list(map(int, input()))
    k = [0]*10
    run = 0
    triplet = 0
    for num in tc:
        k[num] += 1
        if k[num] == 3:
            run += 1
            k[num] -= 3
    for i in range(8):
        if k[i]*k[i+1]*k[i+2] == 1:
            triplet += 1
    if run + triplet == 2:
        print("Baby Gin")
    else:
        print("Lose")