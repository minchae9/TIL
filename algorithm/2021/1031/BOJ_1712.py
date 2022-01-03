A, B, C = map(int, input().split())

start = 1
end = 9999999999

def breakevenpoint(x):
    if (A + B * x) < C * x:
        return True
    return False

ans = 9999999999
while start <= end:
    middle = (start + end) // 2
    if breakevenpoint(middle):
        end = middle - 1
        if middle < ans:
            ans = middle
    else:
        start = middle + 1

if ans == 9999999999:
    ans = -1
print(ans)