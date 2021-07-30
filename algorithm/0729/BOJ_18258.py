# queue
import sys
import collections

N = int(sys.stdin.readline())
queue = collections.deque([])
for i in range(N):
    length = len(queue)
    command = list(sys.stdin.readline().split())
    if command[0] == 'push':
        queue.append(command[1])
    elif command == ['front']:
        if length == 0:
            print(-1)
        else:
            print(queue[0])
    elif command == ['back']:
        if length == 0:
            print(-1)
        else:
            print(queue[-1])
    elif command == ['size']:
        print(length)
    elif command == ['empty']:
        if length == 0:
            print(1)
        else:
            print(0)
    else:
        if length == 0:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
