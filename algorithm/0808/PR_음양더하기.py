def solution(absolutes, signs):
    for i in range(len(signs)):
        if signs[i] == 0:
            absolutes[i] = -absolutes[i]
    return sum(absolutes)