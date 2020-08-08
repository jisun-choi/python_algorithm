#String형 배열 Seoul의 element중 Kim의 위치 x를 찾아, 김서방은 x에 있다는 String을 반환하는 함수, solution을 완성하세요. 
#Seoul에 Kim은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.
# Seoul은 길이 1 이상, 1000 이하인 배열입니다.
# Seoul의 원소는 길이 1 이상, 20 이하인 문자열입니다.
# Kim은 반드시 Seoul 안에 포함되어 있습니다.

def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            return f'김서방은 {i}에 있다'
seoul = ["Jane", "Kim"]

print(solution(seoul))

#좋은 답 
def solution(seoul):
    return '김서방은 {}에 있다'.format(seoul.index('Kim'))
seoul = ["Jane", "Kim"]

print(solution(seoul))



