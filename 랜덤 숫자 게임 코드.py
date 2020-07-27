#1부터 100 사이의 숫자를 하나 랜덤하게 생성하고, 이를 맞추는 게임을 작성
#숫자를 하나 생성하고, 그 다음 사용자가 숫자를 입력하면 이 둘을 비교하여 ‘높음’, ‘낮음’, ‘맞췄다’를 출력
#몇 번의 guess 끝에 답을 맞췄는 지 시도한 횟수를 값으로 출력

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
