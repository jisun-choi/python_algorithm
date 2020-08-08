#피보나치 수열(0 1 1 2 3 5 8 13 21 34 ...)
count = 0 
def fibo(n):
  global count
  count += 1
  if n == 0:
    return 0
  elif n == 1:
    return 1
  elif n == 2:
    return 1
  else:
    return fibo(n-1) + fibo(n-2)
  
print(fibo(0))
print(fibo(1))
print(fibo(2))
print(fibo(3))
print(fibo(4))
print(fibo(5))

for i in range(int(input('n까지 피보나치 수열: '))+1): 
  print(fibo(i),'', end = '')
print('\n연산 횟수: ',count)
    
        