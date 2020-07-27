#예외 처리 문법을 활용하여 정수가 아닌 숫자 입력 시 에러문구 나오는 코드 작성 
print('숫자 입력:',end='')
user_input = input()
if user_input.isnumeric()== True:
    print(user_input)
else:
    print('정수가 아닙니다')
