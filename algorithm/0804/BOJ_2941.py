chars = input()
i = 0
total = 0
while i < len(chars)-1:
    if chars[i]+chars[i+1] in ('lj', 'nj') or chars[i+1] in ('-', '='):
        i += 1
    elif chars[i:i+3] == 'dz=':
        i += 2
    total += 1
    i += 1
if i == len(chars)-1 and 97 <= ord(chars[i]) <= 122:
    total += 1
print(total)

