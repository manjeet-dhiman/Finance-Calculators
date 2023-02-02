# This is a Python program that allows the user to access 
# two different financial calculators: 
# an investment calculator and a home loan repayment calculator.

# needed for math.pow
import math

# take input and make it all lowercase
calculator = input("""Choose either 'investment' or 'bond' from the menu below to proceed:\n\n
investment\t-\tto calculate the amount of interest you'll earn on your investment\n
bond\t\t-\tto calculate the amount you'll have to pay on a home loan\n\n""").lower()

# when investment entered
if (calculator == "investment"):
    deposit = float(input("How much money are you depositing in £?\n"))
    interest_rate = float(input("What is the interest rate (as a percentage)?\n"))
    years = int(input("How many years?\n"))

    # using indented if statement for interest type
    interest = input("Do you want 'simple' or 'compound' interest?\n").lower()
    if interest == "simple":
        # calculate using simple interest rate forumula to 2 decimal places
        # simple interest = deposit * (1 + (interest rate / 100) * years)
        # divide interest rate by 100 to get a decimal
        interest = round(deposit * ((1 + ((interest_rate / 100) * years))), 2)

        print(f"After {years} years your total investment will be £{interest}.")

    elif interest == "compound":
        # calculate compound forumula interest rate using math.pow
        # coumpound interest = deposit * math.pow((1 + (interest rate / 100)), years)
        # rounded to 2 decimal places
        interest = round(deposit * math.pow((1 + (interest_rate / 100)), years), 2)

        print(f"After {years} years your total investment will be £{interest}.")

    # gives user error message when interest type not correctly entered
    else:
        print("You did not enter simple or compound interest.")

# when bond entered
elif (calculator == "bond"):
    value_house = int(input("What is the value of the house in £?\n"))
    interest_rate = float(input("What is the interest rate (as a percentage)?\n"))
    months = int(input("The number of months they plan to take to repay the bond?\n"))

    # monthly interest rate divided by 100 to get decimal
    # interest rate divided by 12 after for each month
    monthly_interest = (interest_rate / 100) / 12

    # bond interest = (monthly_interest . house_value) / (1 - (1 + monthly_interest)^(-months))
    # round to 2 decimal places
    bond_payment = round(((monthly_interest * value_house) / (1 - (1 + monthly_interest) ** (-months))), 2)

    print(f"You will have to pay £{bond_payment} each month over {months} months.")

# when bond or investment not entered give error message
else:
    print("You did not enter investment or bond.")