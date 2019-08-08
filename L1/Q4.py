from math import*
year= input ("Enter a year.\n")
if (int(year)%4 == 0) and (int(year)%100 > 0):
   print("Yes, it is a leap year.")
elif(int(year)%400 == 0):
    print("Yes, it is a leap year")
else:
    print("No, it is not a leap year")

