#josh A
#10/19/23
#working with if else statements
is_leap = False

year=int(input("what year is it? "))
if year % 4 == 0:
    if year % 100 ==0:
        if year % 400 == 0:
            is_leap = True
        else:
            is_leap = False
    else:
        is_leap = True
else:
    is_leap = False

if is_leap == True:
    print(year, " is a leap year")
if is_leap == False:
    print(year," is not a leap year")

