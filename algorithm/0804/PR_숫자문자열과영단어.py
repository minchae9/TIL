def solution(s):
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer = ''
    i = 0
    while i < len(s):
        try:
            int(s[i])
        except:
            a = 0
        else:
            a = 1

        if a != 0:
            answer += s[i]
            i += 1
        else:
            if s[i:i+3] in numbers:
                answer += str(numbers.index(s[i:i+3]))
                i += 3
            elif s[i:i+4] in numbers:
                answer += str(numbers.index(s[i:i+4]))
                i += 4
            else:
                answer += str(numbers.index(s[i:i+5]))
                i += 5
    return int(answer)