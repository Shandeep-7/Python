#Leap year program
year=input("Enter a year")
n=int(year)
if(n%400==0 or  n%100 ==0 or n%4==0):
    print(n , "is a leap year")
else:
    print(n , "is not a leap year")    