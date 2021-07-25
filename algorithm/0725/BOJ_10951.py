a, b = input().split()
while True:
    if bool(a) == True:
        print(int(a) + int(b))
        try:
            a, b = input().split()
        except:
            break