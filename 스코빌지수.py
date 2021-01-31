# =====================런타임 에러 & 효율성 x========================
def solution(scovile, K):
    answer = 0
    while scovile:
        answer += 1
        min_s = min(scovile)
        min_index = [i for i in range(len(scovile)) if scovile[i] == min_s][0]

        del scovile[min_index]
        min_second = min(scovile)
        min_index = [i for i in range(len(scovile)) if scovile[i] == min_second][0]

        del scovile[min_index]
        manipulated = min_s + (min_second * 2)
        scovile.append(manipulated)
        is_ok = [i for i in scovile if i < K]
        if len(is_ok) > 0:
            continue
        else:
            return answer


# ===============런타임 에러 ========================================
def solution(scovile, K):
    answer = 0
    import heapq

    heapq.heapify(scovile)
    while scovile:
        answer += 1
        min_s = heapq.heappop(scovile)

        if min_s >= K:
            return answer
        else:
            min_2 = heapq.heappop(scovile)
            heapq.heappush(scovile, min_s + min_2 * 2)

        if scovile[0] > K:
            return answer
    return -1


# =====================통과=========================================
def solution(scovile, K):
    answer = 0
    import heapq

    heapq.heapify(scovile)
    while True:
        if scovile[0] >= K:
            break
        elif len(scovile) == 0:
            answer = -1
            break
        else:
            min_1 = heapq.heappop(scovile)
            min_2 = heapq.heappop(scovile)
            heapq.heappush(scovile, min_1 + (min_2 * 2))
            answer += 1
    return answer


scovile = [1, 2, 3, 9, 10, 12]

print(solution(scovile, 7))

