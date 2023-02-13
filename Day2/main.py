# Tip Calculator

print("Welcome to the Tip Calculator!")

# 1. Ask the user for the total bill amount
bill = float(input("What was the total bill? $"))

# 2. Ask the user for the desired tip amount
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

# 3. Ask the user for the number of people to split the bill with
people = int(input("How many people to split the bill? "))

# 4. Calculate the tip amount as a decimal
tip_as_percent = tip / 100

# 5. Calculate the total tip amount by multiplying the bill by the tip percentage
total_tip_amount = bill * tip_as_percent

# 6. Calculate the total bill by adding the tip amount to the bill
total_bill = bill + total_tip_amount

# 7. Divide the total bill by the number of people to split the bill with
bill_per_person = total_bill / people

# 8. Round the bill per person to 2 decimal places
final_amount = round(bill_per_person, 2)

# 9. Display the final calculated amount each person should pay
print(f"Each person should pay: ${final_amount}")








