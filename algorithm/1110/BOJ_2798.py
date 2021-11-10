N, M = map(int, input().split())
cards = list(map(int, input().split()))
mx = 0
for i in range(len(cards)):
    for j in range(len(cards)):
        if i != j:
            for k in range(len(cards)):
                if i != k and j != k:
                    if cards[i] + cards[j] + cards[k] <= M:
                        if cards[i] + cards[j] + cards[k] > mx:
                            mx = cards[i] + cards[j] + cards[k]

print(mx)