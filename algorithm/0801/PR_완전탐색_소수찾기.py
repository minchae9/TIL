from itertools import permutations
def solution(numbers):
    str_num = list(numbers)
    all = []
    for i in range(1, len(numbers)+1):
        lst = list(permutations(str_num, i))
        lst = map(''.join, lst)
        all.extend(lst)
    all = list(map(int, all))
    answer = set()
    for num in all:
        if num > 1:
            for i in range(2, num//2+1):
                if (num % i) == 0:
                    break
            else:
                answer.add(num)
        if num == 2:
            answer.add(num)
    return len(answer)
