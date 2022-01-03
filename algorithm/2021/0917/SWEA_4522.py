def palindrome(c):
    length = len(c)
    for i in range(length//2 + 1):
        if c[i] == '?' or c[length-1-i] =='?':
            continue
        elif c[i] != c[length-1-i]:
            return False
    else:
        return True


T = int(input())
for t in range(1, T+1):
    word = input()
    ans = palindrome(word)
    if ans:
        print(f'#{t} Exist')
    else:
        print(f'#{t} Not exist')