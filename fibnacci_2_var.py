f,s=-1,1
count=int(input("enter no :"))
while count>0:
	print(f+s)
	s=f+s
	f=s-f
	count-=1
