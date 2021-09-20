import math
no= int(input("Enter Binary no: "))
Deci = 0
i = 0
while no>0:
	rem = no%10
	Deci=Deci+rem*int(math.pow(2,i))
	no=no//10
	i+=1
else:
	print("Decimal Number is :",Deci)
