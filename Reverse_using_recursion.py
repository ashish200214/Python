def reverseMethod(n,reverse):
    if(n!=0):
        rem = n%10
        reverse = reverse*10+rem
        return reverseMethod(n//10,reverse)
    
    else:
        return reverse


print(reverseMethod(1234,0))