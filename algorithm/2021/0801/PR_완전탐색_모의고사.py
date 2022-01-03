def solution(answers):
    #supoza1
    a1, b1 = divmod(len(answers), 5)
    supoza1 = [1, 2, 3, 4, 5] * a1 + [1, 2, 3, 4, 5][: b1+1]
    score1 = 0
    #supoza2
    a2, b2 = divmod(len(answers), 8)
    supoza2 = [2, 1, 2, 3, 2, 4, 2, 5] * a2 + [2, 1, 2, 3, 2, 4, 2, 5][: b2+1]
    score2 = 0
    #supoza3
    a3, b3 = divmod(len(answers), 10)
    supoza3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * a3 + [3, 3, 1, 1, 2, 2, 4, 4, 5, 5][: b3+1]
    score3 = 0
    
    for i in range(len(answers)):
        if answers[i] == supoza1[i]:
            score1 += 1
        if answers[i] == supoza2[i]:
            score2 += 1
        if answers[i] == supoza3[i]:
            score3 += 1
    
    result = max(score1, score2, score3)
    answer = []
    if result == score1:
        answer.append(1)
    if result == score2:
        answer.append(2)
    if result == score3:
        answer.append(3)
        
    return answer