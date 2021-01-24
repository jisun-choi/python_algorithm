#=========takeawyas==================
- collections.deque: 앞, 뒤로 데이터를 추가, 삭제할 수 있음 & 효율 up 가능 (큐 자료구조에서)
    eg. appendleft(), popleft() etc
- 나는 전체 길이에서 하나씩 빼가면서 푸는 방법을 생각했는 데 답안들 보면 0에서 시작해서 하나씩 더해가는 식으로 풀었다. 
효율성에서 대해서 고민을 많이 해보자.
#====================================



# 내 오답
def solution(prices):
    answer = []
    length = len(prices)
    for i in range(len(prices)):
        if prices[i - 1] <= prices[i]:
            answer.append(length)
        else:
            answer.append(length - 1)
        length -= 1
    answer.append(0)
    del answer[0]
    return answer


# 모델 답안
from collections import deque


def solution(prices):
    prices = deque(prices)
    ans = []
    while prices:
        cnt = 0
        # price 리스트의 맨 첫번째 원소를 잘라서 price 에 할당
        price = prices.popleft()
        # 맨 처음 원소와 나머지 원소를 하나씩 비교 (i = 나머지 원소)
        for i in prices:
            cnt += 1
            if price > i:
                break
        ans.append(cnt)
    return ans
