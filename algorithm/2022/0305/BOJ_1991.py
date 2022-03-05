N = int(input())
main, left, right = ['.']*26, ['.']*26, ['.']*26

def get_idx(char):
    return ord(char) - 65

for _ in range(N):
    m, l, r = input().split()
    idx = get_idx(m)
    main[idx], left[idx], right[idx] = m, l, r
# 전위순회 (m-l-r)
pre = ''
node = 0
course = []
while len(pre) < N:
    if node not in course:
        course.append(node)
    if main[node] not in pre:
        pre += main[node]
    if left[node] != '.' and left[node] not in pre:
        node = get_idx(left[node])
    elif right[node] != '.' and right[node] not in pre:
        node = get_idx(right[node])
    else:
        course.pop()
        node = course.pop()
print(pre)

# 중위순회 (l-m-r)
iin = ''
node = 0
course = []
while len(iin) < N:
    if node not in course:
        course.append(node)
    if left[node] != '.' and left[node] not in iin:
        node = get_idx(left[node])
    else:
        if (left[node] in iin or left[node] == '.') and main[node] not in iin:
            iin += main[node]
        else:
            if right[node] != '.' and right[node] not in iin:
                node = get_idx(right[node])
            else:
                if main[node] not in iin:
                    iin += main[node]
                course.pop()
                node = course.pop()
print(iin)

# 후위순회 (l-r-m)
post = ''
node = 0
course = []
while len(post) < N:
    if node not in course:
        course.append(node)
    if left[node] != '.' and left[node] not in post:
        node = get_idx(left[node])
    elif right[node] != '.' and right[node] not in post:
        node = get_idx(right[node])
    else:
        if main[node] not in post:
            post += main[node]
        course.pop()
        if course:
            node = course.pop()
print(post)