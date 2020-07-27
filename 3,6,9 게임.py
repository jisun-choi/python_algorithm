#3,6,9 게임 실행 코드 
for i in range(1,51):
  str_i = str(i)
  count_369 = 0
# 369의 갯수 세는 로직 
  for x in str_i:
    if(x == '3') or (x == '6') or (x == '9'):
      count_369 += 1 
# 369 갯수에 따라 박수 숫자 
  if count_369 == 0:
    print(str_i)
  else:
    print(str_i, count_369*'짝')
