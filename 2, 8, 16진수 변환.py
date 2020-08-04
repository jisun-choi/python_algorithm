def bi (num):
      binary = []
  while num != 0:
    x = num // 2 
    y = num % 2
    if y == 0:
      binary.append(0)
      num = x
    elif y == 1:
      binary.append(1)
      num = x
    else:
      break
  binary = binary[::-1]
  return binary

