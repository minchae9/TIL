N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
M = int(input())
test = list(map(int, input().split()))

for t in test:
    s = 0
    e = N - 1
    while s <= e:
        mid = (s+e)//2
        if t == numbers[mid]:
            print(1)
            break
        elif t < numbers[mid]:
            e = mid - 1
        elif t > numbers[mid]:
            s = mid + 1
    else:
        print(0)