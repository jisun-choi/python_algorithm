#단어 1개 입력받아 나누어 출력하기 
x = input('')
for c in x:
    print("'"+c+"'")

#시간 입력받아 그대로 출력하기
hour, minute = input().split(':');
print(hour, minute, sep=':')

#주민등록번호 입력받아 '-' 없이 출력하기 
a,b = input().split("-")
print(a+b)

#정수 두 개 입력받아 합 출력하기
a, b = input().split()
a = int(a)
b = int(b)
print(a+b)

#기초연산
a, b = input().split();
a = int(a)
b = int(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print("%.2f" % (a/b))