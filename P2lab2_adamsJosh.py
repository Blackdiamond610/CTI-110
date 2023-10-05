#josh A
#10/5/23
#get float inputs from user
#display producct with 0 decimals
num1=float(input("Variable 1:"))
print(f'{num1:.0f}')
print(f'{num1:.3f}')
num2=float(input("Variable 2:"))
print(f'{num2:.0f}')
print(f'{num2:.3f}')
num3=float(input("Variable 3:"))
print(f'{num3:.0f}')
print(f'{num3:.3f}')
num4=float(input("Variable 4:"))
print(f'{num4:.0f}')
print(f'{num4:.3f}')

print("Results:")
product=float(f"{(num1 * num2 * num3 * num4):.3f}")
average=float(f"{(num1 + num2 + num3 + num4):.3f}")
print(product)
print(average / 4)
product=float(f"{(num1 * num2 * num3 * num4):.0f}")
average=float(f"{(num1 + num2 + num3 + num4):.0f}")
print(product)
print(average / 4)
