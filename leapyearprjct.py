 
# checking a leap year
# condition year should divide by 4, and divide by 100 and 400 then all conditions true ,the year is leap year without any doudt.
# here the condition is If a year is divisible by 4 but not by 100 and not divisible by 400, then it is also a leap year.

year=int(input("enter any year to check:"))


if year%4==0:
    if year%100=0 :
      if year%400 ==0 :
        print(f"{year} is a leap year ") 
      else:
         print(f"{year} is not a leap year ")
    else:
        print(f"{year} is  a leap year")
else:
    print(f"{year} is not leap year...")
