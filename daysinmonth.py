#Counting the number of days in each month
def leapyear(year):
    n=int(year)
    if(n%400==0 or  n%100 ==0 or n%4==0):
        return True
    else:
        return False 
    
def daysinmonths(yr,mnth):
    noOfDays=[31,28,31,30,31,30,31,31,30,31,30,31]
    if leapyear(yr) and mnth==2:
        return 29
    else:
        return noOfDays[mnth-1]
    
yr = int(input("Enter a year : "))
mnth = int(input("Enter a month : "))

daysinmnth = daysinmonths(yr,mnth)
print(daysinmnth)