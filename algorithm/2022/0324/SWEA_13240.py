# 시간초과
T = int(input())
for tc in range(1, T+1):
    H, W, N = map(int, input().split())
    string = input()
    num_letters = len(string)   # 총 글자수
    words = list(string.split())    # 단어 리스트
    max_word_len = 0
    for word in words:
        if len(word) > max_word_len:
            max_word_len = len(word)
    if H >= W:
        X, Y = W, H
    else:
        X, Y = H, W
    
    # 가로 길이보다 글자 수가 많으면 분모가 0이 되므로
    temp = 1
    if W >= num_letters:
        temp = W//num_letters
    mx = min(H // temp, W // max_word_len)

    for length in range(mx, 0, -1):
        x = X//length   # 짧은 변 x줄
        actual_letters = num_letters - (x - 1)
        if len(words) % x == 0:
            y = actual_letters // x
        else:
            y = actual_letters // x + 1
        if y * length > Y:
            continue
        cnt = 0
        i = y*length - 1
        while i < num_letters-1:
            if string[i] != ' ' and string[i+1] != ' ':
                i -= 1
            else:
                if string[i] != ' ':
                    i += 1
                i += y*length
                cnt += 1
        if cnt <= x:
            print(f'#{tc} {length}')
            break
        else:
             continue
    else:
        print(f'#{tc} 0')