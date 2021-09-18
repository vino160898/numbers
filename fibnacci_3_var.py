f,s=-1,1
count=int(input("enter no :"))
while count>0:
	T=f+s
	print(T)
	f=s
	s=T
	count-=1
