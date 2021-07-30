import sys

K = int(input())
book = []
for k in range(K):
    money = int(sys.stdin.readline())
    if money == 0:
        book.pop()
    else:
        book.append(money)
print(sum(book))
