# chars = input().upper()
# mx = chars.count(chars[0])
# ans = []
# for char in chars:
#     if char in ans:
#         pass
#     else:
#         if chars.count(char) > mx:
#             ans=[char]
#         elif chars.count(char) == mx:
#             ans.append(char)
# if len(ans) > 1:
#     print('?')
# else:
#     print(ans[0])

chars = input().upper()
chars_set = set(chars)
times = []
for char in chars_set:
    times.append(chars.count(char))
if times.count(max(times)) > 1:
    print('?')
else:
    idx = times.index(max(times))
    print(chars[idx])
print(chars_set)