#n을 입력받고 1~i까지 합이 n보다 작을 때까지 실행한 후 그 때까지의 합 출력 
n = int(input('정수 입력> ))
sum = 0
i = 1

while sum < n:
    sum += i 
    i += 1

print(sum)

#입력한 정수 n까지 1씩 증가시켜 출력하되 3의 배수인 경우는 출력하지 않도록 
n = int(input('정수 입력'))

for i in range (n+1):
    if i % 3 != 0:
        print(i)
    else: 
        pass

#시작값, 등차, n번째 정수를 입력 받을 때 n 번째 수 구하기
a, d, n = map(int, input('정수 입력> ').split())
series = []

for i in range(n):
    series.append(a+(i*d))

print(series[-1])

#시작값, 등비, n번째 정수를 입력 받을 때 n 번째 수 구하기
a, r, n = map(int, input('정수 입력> ').split())
series = []

for i in range(n):
    series.append(a*(r**i))

print(series[-1])

#시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째인지를 나타내는 정수(n)가 입력될 때,n번째 수를 출력하는 프로그램
a, m, d, n = map(int, input('정수 입력> ').split())
for i in range(n-1):
    a = a*m+d
print(a)


#같은 날 동시 가입한 3명이 규칙적으로 시스템에 들어가 문제를 풀 때 다시 모두 함께 문제를 풀게 되는 날 
a, b, c = map(float,input().split())
d = 1 
while(d%a != 0 or d%b != 0 or d%c !=0):
    d+=1
print(d)