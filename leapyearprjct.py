 
# checking a leap year
# condition year should divide by 4, and divide by 100 and 400 then all conditions true ,the year is leap year without any doudt.
# here the condition is If a year is divisible by 4 but not by 100 and not divisible by 400, then it is also a leap year.

checkagain=True
print("\u001b[31m Hello!!! , Welcome to Leap year check App \n")

def check_leapyear(year):
  if year%4==0:
      if year%100==0 :
        if year%400 ==0 :
          print(f"{year} is a leap year ") 
        else:
          print(f"{year} is not a leap year ")
      else:
          print(f"{year} is  a leap year")
  else:
      print(f"{year} is not leap year...")

while checkagain:
  year=int(input("Enter year to check whether it is leap year or non-leap year:"))
  check_leapyear(year)
  check=input("Do you want to check another year type Y or N: ").lower()
  if check=="y":
    checkagain=True
  else:
    checkagain=False  

  