# a, b, c = map(int, input().split('.'))

# print("%04d"%a, end='.')  # 4자리. 4자리가 안되면 0으로 채우기
# print("%02d"%b, end='.')  # 2자리. 2자리가 안되면 0으로 채우기
# print("%02d"%c)

a, b, c = map(str, input().split('.'))
print(a.zfill(4)+'.'+b.zfill(2)+'.'+c.zfill(2))