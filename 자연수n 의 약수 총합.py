#자연수 n을 입력하고, 자연수 n의 약수들의 총 합을 구하시오.

n = int(input('자연수 입력: '))
total = []

if n > 0:
    for i in range(1,n+1):
        if n % i == 0:
            total.append(i)
    print('%d의 약수'% n,total)
    print('%d의 약수의 합'% n,sum(total))

elif n <= 0:
    print('%d :자연수 아님'% n)