def checkLeap(year):
  if(year%400==0 && (year%4==0&&year%100!=0)):
    print("Leap Year")
  else:
    print("Not Leap Year")

year = int(input("Enter year"))
checLeap(year)
