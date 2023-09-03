def Increment(n):
    return n + 1


def reverseMethod(n):
	reverse = 0
	while(n!=0):
		rem = n%10
		reverse=reverse*10+rem
		n = n//10
	return reverse


def Increment1InDigit(n):
    value = 0
    while n != 0:
        rem = n % 10
        value = value * 10 + Increment(rem)
        n = n // 10  # Use floor division here to get integer results
		# floor division removes the .value Ex . 123.4 = (floor) 123 

    print(reverseMethod(value))

n = 1234
Increment1InDigit(n)