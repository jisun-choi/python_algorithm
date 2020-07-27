#사용자로부터 달러 또는 위안 금액을 입력 받은 후 이를 원으로 바꿔서 계산
#사용자는 100 달러, 100 위안 과 같이 금액과 통화 명 사이에 공백을 넣어 입력
#각 통화 별 환율:  달러- 1112원, 위안 - 171원 

import random

rd_num = random.randint(1,100)
user_num = int(input('숫자 입력: '))
count = 0 

while True:
  count += 1
  if rd_num > user_num:
    print ('높음')
    user_num = int(input('숫자 입력: '))
  elif rd_num < user_num:
    print ('낮음')
    user_num = int(input('숫자 입력: '))
  else:
    print ('맞췄다')
    break 

print('%d번 시도'% count)
