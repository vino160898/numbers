no1, no2 = 100,120
div = 3
count = 0
small = no1 if no1<no2 else no2
while div<no2:
  if no1%div==0 and no2%div==0:
    print(div)
    count+=1
  div+=1
