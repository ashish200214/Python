#program to check user entered number is positive or not
#using brute force method
n = int(input("Enter the Number"))

if(n<0):
	print("number is negative")
elif(n==0):
	print("Number is zero")
else:
	print("Number is Positive")



#using nested if-else
n = int(input("Enter the number"))
if(n>=0):
  if(n==0):
    print("Number is zero")
  else:
    print("Number is positive")
else:
  print("Number is negative")

#using ternary operator

n = (int)input("Enter the number")
print("Positive" if num>=0 else "Negative")
