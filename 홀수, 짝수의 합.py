#1~30 사이의 수에서 홀수만 더한 값, 짝수만 더한 값
i = 1 
even = 0 
odd = 0

while i < 31: 
  if i % 2 == 0:
     even += i
  else: 
    odd += i
  i += 1 

print('짝수 더한 값: ', even)
print('홀수 더한 값: ', odd)
