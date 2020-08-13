#0이 입력될 때까지 무한 출력
a = map(int, input().split())

for i in a:
    if i != 0:
       print(i)
    else:
       break

#정수 1개 입력받아 카운트 다운 출력
a = int(input())
while a > 1 :
    print(a-1)
    a -= 1

#영문자(a~z)가 입력되었을 때 그 문자까지의 알파벳을 순서대로 출력 
a = ord(input())
b = ord('a')
while a>=b :
    print(chr(b),end = ' ')
    b=b+1  
#정수 1개 입력받아 그 수까지 쭉 출력
a = int(input())
b = int(0)
while a>=b :
    print(b)
    b = b+1

#짝수까지 합 출력
a = int(input())
s = 0
for i in range(1,a+1) :
    if(i%2==0) :
        s+=i
print(s)

#1,2,3,,,을 계속 더할 때 그 합이 입력한 정수보다 같더나 작을 때까지 계속 더하는 프로그램
a = int(input())
c = 0
for i in range(1,a+1) :
    c+=i
    if c>=a:
        print(i)
        break