from math import*
year= input ("What is the year?\n")
if (int(year)/4 - abs(int(year)/4) == 0) and (int(year)/400-abs(int(year)/400) == 0):
   print("Yes, it is a leap year.")
elif (int(year)/100-abs(int(year)/100) == 0):
    print("No, it is not a leap year")

