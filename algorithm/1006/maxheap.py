"""
배운 내용
"""

def enq(n):
    global last
    last += 1
    tree[last] = n
    c = last
    p = c//2
    while p>=1 and tree[p]<tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c//2

def deq():
    global last
    tmp = tree[1]
    tree[1] = tree[last]
    last -= 1
    p = 1
    c = 2 * p  # 왼쪽자식번호를 먼저 계산해서

    while c <= last: # 왼쪽 자식이 있는지 확인
        if c + 1 <= last and tree[c] < tree[c + 1]: # 오른쪽 자식도 있고 오른쪽이 더 작으면 선택
            c += 1 # 더 큰 자식이 됨
        if tree[p] < tree[c]:  # 부모와 자식 비교
            tree[p], tree[c] = tree[c], tree[p] # 자식이 더 작으면 교환
            p = c           # 자리 바꿔서 자식 자리로 간 값과 그 자리의 자식번호 계산
            c = p * 2
        else:
            break
    return tmp

tree = [0] * 101
last = 0