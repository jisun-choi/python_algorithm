x = input('input str> ')
pairs = []

for i in x:
      if len(pairs) == 0:
            pairs.append(i)
      elif pairs[-1] == i:
            pairs.pop()
      else:
            pairs.append(i)
if len(pairs) == 0:
      print(1)
else:
      print(0)


    

        
        