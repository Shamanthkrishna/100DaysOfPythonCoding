#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
total_bill=float(input("Welcome to the tip calculator.\nWhat was the total bill? $"))
tip=int(input("What percentage of tip would you like to give? 10, 12, or 15? "))
people=int(input("How many people to split the bill? "))
tip_amount=(tip/100)+1
final_bill=(total_bill/people) * tip_amount
#or use round function
#final_amount=round(final_bill,2)
final_amount="{:.2f}".format(final_bill)
print(f"Each person should pay: ${final_amount}")