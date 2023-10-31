num_1=int(input("enter a number: "))
num_2=int(input("enter another number: "))

if num1 <= num2:
    for item in range(num1,num2 + 1,5) :
        print(item)

else:
    print("please try again, this time with the first number smaller")
