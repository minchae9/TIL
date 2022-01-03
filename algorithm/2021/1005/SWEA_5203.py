T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    A = [cards[0], cards[2], cards[4]]
    B = [cards[1], cards[3]]
    turn = 5
    ans = 0
    flag = False
    while turn <= 12:
        if flag:
            break
        if turn % 2:    # A가 카드를 받음
            A.sort()
            for i in range(len(A) - 2):
                if A[i] == A[i + 1] == A[i + 2] or (A[i]+1 in A and A[i]+2 in A):
                    ans = 1
                    flag = True
                    break
            B.append(cards[turn])
        else:   # B가 카드를 받음
            B.sort()
            for i in range(len(B) - 2):
                if B[i] == B[i + 1] == B[i + 2] or (B[i]+1 in B and B[i]+2 in B):
                    ans = 2
                    flag = True
                    break
            if turn < 12:
                A.append(cards[turn])
        turn += 1
    print(f'#{tc} {ans}')