no= int(input("Enter Decimal no: "))
binaryNo=''
while no>0:
	binaryNo = str(no%2)+binaryNo
	no=no//2
else:
	print("binary number is ",binaryNo)
