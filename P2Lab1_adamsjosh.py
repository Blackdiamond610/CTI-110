miles = float(input())
gas = float(input())
mpg = gas/miles

gas_cost1= (mpg)* 20
gas_cost2= (mpg)* 75
gas_cost3= (mpg)* 500

print(f'{gas_cost1:.2f} {gas_cost2:.2f} {gas_cost3:.2f}')
