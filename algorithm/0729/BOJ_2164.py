import sys
import collections

N = int(sys.stdin.readline())
cards = collections.deque([])

for num in range(1, N+1):
    cards.append(num)
for i in range(2 * N):
    if len(cards) == 1:
        print(cards[0])
        break
    if i % 2:
        a = cards.popleft()
        cards.append(a)
    else:
        cards.popleft()
        
    