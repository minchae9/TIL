# Pypy로 채점
"""
n666
666n

nn666
n666n
666nn

nnn666
nn666n
n666nn
666nnn

...

"""
N = int(input())

movies = [666]  # 3자리수
k = 3
flag = False
while len(movies) <= 10000:
    k += 1
    movies.append(666*(10**(k-3)))  # 끝자리 00인 애들은 따로 넣어줌

    for i in range(k-3, -1, -1):    # 연속 3개의 6을 가능한 자리에 넣어주고
        num = [-1] * k
        num[i] = num[i+1] = num[i+2] = 6

        # n에 채워넣을 숫자
        for n in range(10**(k-3)):
            if len(str(n)) < k-3:
                gap = k-3-len(str(n))
                n = '0' * gap + str(n)
            else:
                n = str(n)
            # make는 num을 복사
            make = []
            for item in num:
                make.append(item)
            # 숫자 정해지지 않은 자리에 숫자 채워주기
            idx = 0
            for j in range(k):
                if idx >= k-3:
                    break
                if make[j] < 0:  # 숫자 정해지지 않은 자리
                    make[j] = int(n[idx])
                    idx += 1
            # 무비 넘버에 하나씩 추가
            movie_num = ''
            for m in range(k):
                movie_num += str(make[m])
            if int(movie_num) not in movies:
                movies.append(int(movie_num))
    # 출력
    if len(movies) >= N:
        movies.sort()
        print(movies[N-1])
        break