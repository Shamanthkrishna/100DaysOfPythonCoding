# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total=0
if size=="S" and add_pepperoni=="Y":
    total+=17
if size=="S" and add_pepperoni=="N":
    total+=15
if size=="M" and add_pepperoni=="Y":
    total+=23
if size=="L" and add_pepperoni=="Y":
    total+=28
if size=="M" and add_pepperoni=="N":
    total+=20
if size=="L" and add_pepperoni=="N":
    total+=25
if extra_cheese=="Y":
    total+=1
if extra_cheese=="N":
    total+=0
print(f"Your final bill is: ${total}.")