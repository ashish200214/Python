def greatest(num1,num2,num3):
   
        if(num1>=num3 and num1>=num2):
            print("Num1 is greatest")
        elif(num2>=num1 and num2>=num3):
            print("Num2 is greatest")
        else:
            print("Num3 is greatest")



num1 = int(input("Enter first num :- "))
num2 = int(input("Enter second num :- "))
num3 = int(input("enter third num :- "))

greatest(num1,num2,num3)
        
