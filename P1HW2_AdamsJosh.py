#Josh
#10/2/2023
#Basic math on numbers entered
print("This program calculates and displays travel expenses")
budget = int(input("enter Budget"))
trvl_dest =input("Enter your travel destination")
gas_est=int(input("How much will you spend on gas?"))
hotel_price=int(input("How much will you spend for hotels"))
food_price=int(input("how much for food?"))
print("--------Travel Expenses--------")
print("Location:",trvl_dest)
print("Initial Budget:",budget)
print("fuel:",gas_est)
print("accomodation:",hotel_price)
print("Food:",food_price)
print("Remaining Balance:",-budget + gas_est + hotel_price + food_price )

