import sys

N = int(sys.stdin.readline())

def letter_sum(num):
    res = 0
    n = len(str(num)) - 1
    while n >= 0:
        quo, rem = divmod(num, 10 ** n)
        res += quo
        num = rem
        n -= 1
    return res

# def letter(num):
#     k = 0
#     for a in range(len(str(num))):
#         k += int(str(num)[a])
#     return k

for i in range(N):
    if i + letter_sum(i) == N:
        print(i)
        break
else:
    print(0)

# print(letter(198))   