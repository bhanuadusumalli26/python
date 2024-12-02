#check Leap year or not
year=int(input("enter a year: "))
#divided by 100 means century  year
#century year divided by 400 is Leap year
if (year%400==0) and (year%100==0):
    print("{0} is a leap year".format(year))
#not divided by 100 means not a century year
#year divided by 4 is a leap year 
elif (year%4==0) and (year%100!=0):
    print("{0} is a leap year".format(year))
#if not divided by both 400 and 4 then it is not a leap year
else:
    print("{0} is not a leap year".format(year))
