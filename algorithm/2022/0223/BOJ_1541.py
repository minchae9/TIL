# '-'가 있으면 뒤에 오는 '+'는 모두 '-'가 될 수 있다. & 기호 뒤에 바로 이어지는 0들은 추가하지 않는다.
equation = input()
new = ''
flag = False
is_zero = True
for i in range(len(equation)):
    if equation[i] == '0' and is_zero:
        pass
    else:
        if equation[i] == '-':
            flag = True
            is_zero = True
            new += '-'
        elif equation[i] == '+':
            if flag:
                new += '-'
            else:
                new += '+'
            is_zero = True
        else:
            is_zero = False
            new += equation[i]
print(eval(new))