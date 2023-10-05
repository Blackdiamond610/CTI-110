#Josh A
#10/5/23
#dictionary
First_name=input("Enter First name")
Hair_color=input("Enter Hair Color")
Eye_color=input("Enter Eye Color")
Height=float(input("Enter Height"))
Age=int(input("Enter Age"))
Fav_food=input("Enter Favorite Food")

#create dictionary
user_traits={"First name":First_name, "Hair color":Hair_color,"Eye Color":Eye_color,"Height":Height,"Age":Age,"Favorite Food":Fav_food}
print(f"{user_traits['First name']}is a {user_traits['Height']}tall student with {user_traits['Hair color']} and {user_traits['Eye Color']}. They are {user_traits['Age']} years old and their favorite food is {user_traits['Favorite Food']}.")
