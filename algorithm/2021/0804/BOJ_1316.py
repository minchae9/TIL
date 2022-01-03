N = int(input())
total = 0
for k in range(N):
    word = input()
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            continue
        else:
            if word[i] in word[i+2:]:
                break
            else:
                continue
    else:
        total += 1
print(total)
