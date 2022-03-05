# 더 효율적인 풀이

출처: [goofy1 님의 풀이](https://www.acmicpc.net/source/28233297)

```python
import sys

def pre_order(node):
  if node == '.':
    return
  print(node, end='')
  pre_order(tree[node][0])
  pre_order(tree[node][1])

def post_order(node):
  if node == '.':
    return
  post_order(tree[node][0])
  print(node, end='')
  post_order(tree[node][1])

def in_order(node):
  if node == '.':
    return
  in_order(tree[node][0])
  in_order(tree[node][1])
  print(node, end='')

N = int(sys.stdin.readline())
tree = {}

for _ in range(N):
  node, left, right = sys.stdin.readline()[:-1].split(' ')
  tree[node] = [left, right]

pre_order('A')
print()
post_order('A')
print()
in_order('A')
```

tree를 딕셔너리 자료구조로 만들면 문자를 인덱스로 사용할 필요가 없다!

(딕셔너리는 내가 잘 사용하지 못하는 구조 중 하나다. 필요한지 확인하고 그렇다면 써보도록 하자.)

전위순회, 중위순회, 그리고 후위순회에 대한 정석적인 함수형태다. (위 코드에서는 후위순회와 중위순회 코드가 뒤바뀌어 있음에 주의!)


