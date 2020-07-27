#input 함수로 로그인 성공/실패 코드 작성 
id = 'id'
pw = 'pw'
user_id = input('id?')
user_pw = input('pw?')

if (user_id == id) and (user_pw == pw):
  print('로그인 성공')
else:
  print('로그인 실패')
