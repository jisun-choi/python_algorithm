#당신은 kakao 서비스를 이용하는 택시 기사입니다. 50명의 승객과 매칭 기회가 있을 때, 아래 조건을 만족하는 승객 수를 구하시오.
#조건 1: 승객별 운행 소요 시간은 5~50분 사이의 난수로 정해집니다.
#조건 2: 당신은 소요 시간 5~15분 사이의 승객만 매칭해야 합니다.

from random import *

def case():
    my_guest ={}
    for i in range(1, 51):
        my_guest[f'{i}번째 손님'] = randrange(5,51)
    return my_guest

print(case())

case_all = case()
pick = case_all.values()
matching = range(5,15)

count = 1
for i in pick:
    if i in matching:
        count += 1

for i in case_all:
    print(i, case_all[i])
print(f'총 탑승 승객: {count}')


