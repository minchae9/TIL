def solution(today, org_terms, privacies):
    answer = []
    # 약관 유효기간 dictionary로
    terms = dict()
    for org_term in org_terms:
        k, v = org_term.split()
        terms[k] = v
    # 유효기간 계산하여
    for i in range(len(privacies)):
        privacy = privacies[i]
        join_dt, term = privacy.split()
        dur = int(terms[term])
        # 오늘 이전인지 확인
        join_dt = join_dt.replace(".", "")
        month = int(join_dt[4:6])
        ## 12월
        if (month + dur) % 12 == 0:
            plus_year, f_month = (month + dur) // 12 - 1, 12
        else:   ## 12월 외
            plus_year, f_month = (month + dur) // 12, (month + dur) % 12
        f_year = int(join_dt[0:4]) + plus_year
        ## 1일 -> 보유기간은 그 전달 28일까지
        if join_dt[-2:] == "01":
            f_day = "28"
            f_month -= 1
        else:
            f_day = ("0" + str(int(join_dt[-2:]) - 1))[-2:]
        ## 일 조정하면서 월이 0월 되면 -> 그 전해 12월
        if f_month == 0:
            f_month = "12"
            f_year -= 1
        else:
            f_month = ("0" + str(f_month))[-2:]
        due_date = str(f_year) + f_month + f_day
        if today.replace(".", "") > due_date:
            answer.append(i+1)
        # print("due_date: " + due_date)
    return answer


# 한 달을 28일로 정해둔 걸 이용하면 더 똑똑하게 할 수 있다.
# https://school.programmers.co.kr/learn/courses/30/lessons/150370/solution_groups?language=python3