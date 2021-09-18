no = 100
div = 2
count = 0
while div<no:
  if no%div==0:
    print(div)
    count+=1
  div+=1

print("No. of divisors are ", count)
if count==0:
    print("Prime Number ")
else:
    print("Not Prime Number")
