idx = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'],
 ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
word = input()
time = 0

for i in range(len(word)):
    for j in range(len(idx)):
        if word[i] in idx[j]:
            time += (j+3)
            break
print(time)