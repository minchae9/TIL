A = int(input())
B = int(input())
C = int(input())
num = A*B*C
arr = [0]*10
for i in range(10):
    print(str(num).count(str(i)))
