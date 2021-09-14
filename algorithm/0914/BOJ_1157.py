word = input().upper()
d = {}
q = []
mx = 1
for i in word:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
for c in d.keys():
    if d[c] > mx:
        mx = d[c]
        q = []
        q.append(c)
    elif d[c] == mx:
        q.append(c)
if len(q) > 1:
    print('?')
else:
    print(q[0])