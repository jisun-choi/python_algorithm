# 모델답안
def solution(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]


def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    oc = tc = thc = 0
    for i in range(len(answers)):
        if answers[i] == one[i % len(one)]:
            oc += 1
        if answers[i] == two[i % len(two)]:
            tc += 1
        if answers[i] == three[i % len(three)]:
            thc += 1
        highest = max(oc, tc, thc)
    answer = []
    if highest == oc:
        answer.append(1)
    if highest == tc:
        answer.append(2)
    if highest == thc:
        answer.append(3)
    return answer


answers = [1, 2, 3, 4, 5]
print(solution(answers))
