#1~n, 1~m까지 있는 주사위 2개를 던졌을 때 나올 수 있는 모든 경우의 수
a, b = map(int, input().split())
for i in range(1, a+1):
    for j in range(1, b+1):
        print(i, j)

#2~n단까지 구구단 출력
n = int(input())
for i in range(2, n+1):
    for j in range(1, 10):
        print(f'{i} * {j}  ={i*j}')

#rgb 빛 섞어 색 만들기
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
d = 0
for i in range(a):
    for j in range(b):
        for k in range(c):
            print(i,j,k)
            d+=1
print(d)
