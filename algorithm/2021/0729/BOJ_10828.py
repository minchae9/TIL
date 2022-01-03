# stack
import sys

N = int(input())
stack = []
for i in range(N):
    command = list(sys.stdin.readline().split())  
    if command[0] == 'push':
        stack.append(command[1])
    elif command == ['top']:
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
    elif command == ['size']:
        print(len(stack))
    elif command == ['empty']:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command == ['pop']:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()