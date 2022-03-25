## '빙글빙글빙글'님 정답 코드 참고함
T = int(input())
for tc in range(1, T + 1):
    H, W, N = map(int, input().split())
    string = input()
    num_letters = len(string)  # 총 글자수
    words = list(string.split())  # 단어 리스트
    max_word_len = 0
    for word in words:
        if len(word) > max_word_len:
            max_word_len = len(word)

    mx = W // max_word_len  # 글자의 최대 크기

    # 여기서부터 코드 참고함
    ans = 0
    for length in range(mx, 0, -1):
        h, w = 1, 0     # 1행의 처음(0번째)에서 시작
        for word in words:
            if w == 0:  # 처음에 첫 단어 그냥 넣기
                w += len(word) * length
            else:
                # 해당 줄에 기존에 있는 단어들의 길이 + 사이 공백 + 이번 단어 길이가
                # 너비를 넘을 경우 -> 다음 줄로 내려야 함
                if w + len(word) * length + length > W:
                    h += 1  # 현재 위치한 행 (즉, 행을 하나 추가한 것)
                    w = len(word) * length  # 새로운 행엔 이번 단어 하나만
                else:
                    w += length + len(word)*length # 너비 넘지 않으므로 공백과 단어 그대로 추가
        if h * length <= H and w <= W:  # 가로 세로 초과하지 않은 경우 -> 종료
            ans = length
            break
    print(f'#{tc} {ans}')