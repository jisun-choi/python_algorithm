#사이트별로 비밀번호를 만들어 주는 프로그램을 작성
#규칙1: http:// 부분제거 → naver.com
#규칙2: 처음 만나는 점(.) 이후 부분 제거 → naver
#규칙3: 남은 글자 중 처음 3글자(nev) + 글자수(5) +글자 내 'e'의 갯수(1) + '!'

def Password(site):
    rule = site[7:]
    pre = rule.split('.')[0][:3]
    num = len(rule.split('.')[0])
    count = 0
    for i in rule:
        if  'e' in i:
            count += 1
    password = pre, str(num), str(count),'!'
    show = ''.join(password)
    return show

x = input('사이트: ')
print(Password(x))
