while True:
    sentence = input()
    if sentence == '.':
        break
    else:
        stack = []
        for c in sentence:
            if c in ('(', '['):
                stack.append(c)
            elif c == ')':
                if len(stack) == 0 or stack.pop() != '(':
                    print('no')
                    break
            elif c == ']':
                if len(stack) == 0 or stack.pop() != '[':
                    print('no')
                    break
        else:
            if stack:
                print('no')
            else:
                print('yes')