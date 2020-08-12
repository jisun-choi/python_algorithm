#1(true, 참) 또는 0(false, 거짓) 이 입력되었을 때 반대로 출력하는 프로그램
a = input()
x = int(a)
b = bool(x)
print(b)
x = int(not b)
print(x)

#정수 3개 입력받아 짝수만 출력 

a = map(int, input().split())
for x in a:
    if x % 2 == 0:
        print(x)