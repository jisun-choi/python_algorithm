#13자리의 주민 등록번호를 입력 후 성별(남자, 여자)를  출력하는 프로그램을 작성
id_num = input('id #?')
gender = id_num[7]

if gender == ('1' or '3'):
    print('male')
if gender == ('2' or '4'):
    print('female')

#id_num[-7]로 뒤에서부터 값을 세서 받으면 입력 시 - or 공백을 넣지 않더라도 오류 없이 결괏값 출력 가능 