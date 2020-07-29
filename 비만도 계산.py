#임의의 체중과 신장을 입력한후 비만도를 출력하는 함수를 작성
#(BMI 공식활용 weight/heigth**2)

weight = int(input('weight?'))
height = int(input('height?'))
BMI = (weight/height**2)*10000
print('BMI = %.1f'% BMI)

if BMI <18.5:
    print('마른체형')
    
elif 18.5 <= BMI < 25.0:
    print('표준')
    
elif 25.0 <= BMI < 30.0:
    print('비만')

else:
     print('고도 비만')