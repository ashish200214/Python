#printing sum of natural number

def sumOfno(n):
	sum=0
	for i in range(1,n+1):
		sum=sum+i
	
	return sum

def recursion(n):
	sum=0
	if(n!=0):
		sum=sum+n
		return sum+recursion(n-1)
	else:
		return sum

n = int(input("Enter the No :-"))
print(recursion(n))
