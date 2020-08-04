num = input('카드번호를 입력하세요(하이픈 필수)> ')
split_list = num.split('-')

split_list[0] = '****'
split_list[3] = '****'

split_list = '-'.join(split_list)
print(split_list)



